

/etc/systemd/system/gracc-backup-raw.service: gracc-backup-raw.service
	cp gracc-backup-raw.service /etc/systemd/system/gracc-backup-raw.service


/etc/systemd/system/gracc-backup-raw.timer: gracc-backup-raw.timer
	cp gracc-backup-raw.timer /etc/systemd/system/gracc-backup-raw.timer


/etc/systemd/system/gracc-backup-transfer.service: gracc-backup-transfer.service
	cp gracc-backup-transfer.service /etc/systemd/system/gracc-backup-transfer.service


/etc/systemd/system/gracc-backup-transfer.timer: gracc-backup-transfer.timer
	cp gracc-backup-transfer.timer /etc/systemd/system/gracc-backup-transfer.timer

/etc/systemd/system/gracc-backup-ps.timer: gracc-backup-ps.timer
	cp gracc-backup-ps.timer /etc/systemd/system/gracc-backup-ps.timer

/etc/systemd/system/gracc-backup-ps.service: gracc-backup-ps.service
	cp gracc-backup-ps.service /etc/systemd/system/gracc-backup-ps.service


/etc/systemd/system/gracc-backup-ps-itb.timer: gracc-backup-ps-itb.timer
	cp gracc-backup-ps-itb.timer /etc/systemd/system/gracc-backup-ps-itb.timer

/etc/systemd/system/gracc-backup-ps-itb.service: gracc-backup-ps-itb.service
	cp gracc-backup-ps-itb.service /etc/systemd/system/gracc-backup-ps-itb.service



/usr/bin/gracc-backup: gracc-backup
	cp gracc-backup /usr/bin/gracc-backup

/var/lib/graccarchive/secondary:
	mkdir /var/lib/graccarchive/secondary
	chown gracc: /var/lib/graccarchive/secondary

/var/lib/graccarchive/secondary-transfer:
	mkdir /var/lib/graccarchive/secondary-transfer
	chown gracc: /var/lib/graccarchive/secondary-transfer



install: /etc/systemd/system/gracc-backup-raw.service /etc/systemd/system/gracc-backup-transfer.service /etc/systemd/system/gracc-backup-raw.timer /etc/systemd/system/gracc-backup-transfer.timer /usr/bin/gracc-backup /var/lib/graccarchive/secondary /var/lib/graccarchive/secondary-transfer
	

uninstall: 
	rm -f /etc/systemd/system/gracc-backup-raw.service /etc/systemd/system/gracc-backup-transfer.service /etc/systemd/system/gracc-backup-raw.timer /etc/systemd/system/gracc-backup-transfer.timer /usr/bin/gracc-backup


