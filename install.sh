#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] Checking files..."
[ -f bcbs ] || { echo "[ERROR] bcbs not found"; exit 1; }
[ -f terminal.py ] || { echo "[ERROR] terminal.py not foun"; exit 1; }

echo "[+] Instaling BCBS-NetHunter..."
chmod +x bcbs terminal.py
cp bcbs $PREFIX/bin/bcbslauncher
echo "[ OK ] Type: bcbslauncher"
