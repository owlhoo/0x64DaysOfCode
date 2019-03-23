#!/usr/bin/env bash

python3 raspored_downloader.py

md5sum raspored.pdf > new_hash

if [[ ! -e old_hash ]]
then
    touch old_hash
fi

if ! diff old_hash new_hash
then
	cat new_hash > old_hash
	cp raspored.pdf $HOME/Desktop/novi_raspored.pdf
	custom=''
	echo "* - required"
	echo "Enter sender email, password, receiver email and  (optional) custom message, please:"
	read sender password receiver
	python3 notify.py ${sender} ${password} ${receiver} 2>> error_log.txt
else
	echo isti su
fi