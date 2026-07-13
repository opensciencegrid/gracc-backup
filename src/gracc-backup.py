import sys
import tomllib
import os
import subprocess
import re
import time

# Should be either raw, transfer, ps-itb, or ps-prod
id = sys.argv[1]

def backup_archive(file_path, file_name):
    toml_path = f'/app/config/gracc-archive-{id}.toml'
    with open(toml_path, 'rb') as f:
        toml_text = tomllib.load(f)
        output_path = toml_text['Directories']['dest']      
    local_full_path = 'file://' + file_path + '/' + file_name
    remote_full_path = output_path + file_name
    if (os.environ.get('X509_USER_CERT') == None):
        os.environ['X509_USER_CERT'] = '/backup-cert/tls.crt'
    if (os.environ.get('X509_USER_KEY') == None):
        os.environ['X509_USER_KEY'] = '/backup-cert/tls.key'
    print(subprocess.check_output(['gfal-copy', "--force", local_full_path, remote_full_path], timeout=600))

    # Verify archive was succesfully copied
    unformatted_remote_checksum = subprocess.check_output(f'gfal-sum -v {remote_full_path} MD5', shell=True).decode('utf-8')
    remote_checksum = re.findall('.+ (.+)\\n', unformatted_remote_checksum)[0]
    unformatted_local_checksum = subprocess.check_output(f'md5sum {file_full_path}', shell=True).decode('utf-8')
    local_checksum = re.findall('(.+)  .+', unformatted_local_checksum)[0]
    
    return remote_checksum == local_checksum

def purge_old_archive(file_path):
    file_time = os.stat(file_path).st_mtime
    four_days_ago = time.time() - (60 * 60 * 24 * 4)
    if file_time < four_days_ago:
        os.remove(file_path)

input_path = f'/data/{id}/output'
secondary_path = f'/data/{id}/secondary'
# Search through archives output folder
for file in os.listdir(os.fsencode(input_path)):
    file_name = os.fsdecode(file)
    file_full_path = input_path + '/' + file_name
    file_size = os.stat(file_full_path).st_size

    if not file_name.endswith('tar.gz'):
        # Ignore non archive files
        pass
    elif file_size == 0:
        purge_old_archive(file_full_path)
    elif file_size < 300:
        # Remove bad files
        os.remove(file_full_path)
    else:
        if backup_archive(input_path, file_name):
            os.rename(file_full_path, secondary_path + '/' + file_name)
            os.mknod(file_full_path)
        else:
            print('Error: Failed checksum comparison')

# Clean up old secondary archives
for file in os.listdir(os.fsencode(secondary_path)):
    file_name = os.fsdecode(file)
    file_full_path = secondary_path + '/' + file_name
    purge_old_archive(file_full_path)