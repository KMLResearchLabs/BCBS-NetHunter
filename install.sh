#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] Instalando BCBS-NetHunter..."

TERMINAL_PY="data/data/com.termux/files/home/BCBS-NetHunter/BLKCR Net/terminal.py"

chmod +x bcbslauncher
[ -f "$TERMINAL_PY" ] && chmod +x "$TERMINAL_PY" || echo "[!] terminal.py don't found..."

cp bcbs $PREFIX/bin/bcbslauncher

echo "[ OK ] BCBS-NetHunter is ready"
echo "type: bcbslauncher"
