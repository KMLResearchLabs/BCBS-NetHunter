#!/data/data/com.termux/files/usr/bin/bash

cd BCBS-NetHunter
git reset --hard HEAD
git fetch
git status
git diff
git pull
pip install requests
pip install dnspython
pip install python-whois
pip install phonenumbers
pip install colorama
