#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] Getting interpreter"
pkg update -y && pkg install python -y

echo "[+] Getting libs"
pip install requests dnspython python-whois phonenumbers colorama

echo "[+] Getting BCBS-NetHunter Launcher..."
chmod +x bcbslauncher.sh
cp bcbslauncher.sh $PREFIX/bin/bcbs
chmod +x $PREFIX/bin/bcbs

echo "[+] Setting GitMancer..."

chmod +x gitmancerINS.sh gitmancerRST.sh gitmancerUPT.sh
ln -sf gitmancerINS.sh $PREFIX/bin/bcbs-upgrade
ln -sf gitmancerRST.sh $PREFIX/bin/bcbs-upgrade-rst
ln -sf gitmancerUPT.sh $PREFIX/bin/bcbs-update
chmod +x $PREFIX/bin/bcbs-*

echo "[ OK ] Command installation finished"
echo "Type 'bcbs' to initialize BCBS-NetHunter"
hash -r