#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] Instaling BCBS-NetHunter..."

chmod +x bcbs
chmod +x terminal.py

cp bcbs $PREFIX/bin/bcbslauncher

echo "[ OK ] BCBS NetHunter is ready to use"
echo "To start type: bcbs"
