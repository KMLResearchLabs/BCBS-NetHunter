echo "[+] Getting BCBS-NetHunter Launcher..."

chmod +x bcbslauncher.sh

echo "[+] Giving permission..."

cp bcbslauncher.sh $PREFIX/bin/bcbs

echo "[+] Setting command..."

echo "[ OK ] Command installation finished"
echo "Type "bcbs" to inicializate BCBS-NetHunter"

hash -r
