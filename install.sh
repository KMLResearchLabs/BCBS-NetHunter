echo "[+] Getting interpreter"
pkg install python

echo "[+] Getting libs"
pip install requests
pip install dnspython
pip install python-whois
pip install phonenumbers
pip install colorama


echo "[+] Getting BCBS-NetHunter Launcher..."

chmod +x bcbslauncher.sh

echo "[+] Giving permission..."

cp bcbslauncher.sh $PREFIX/bin/bcbs

echo "[+] Setting command..."



chmod +x gitmancerINS.sh
chmod +x gitmancerRST.sh
chmod +x gitmancerUPT.sh

echo "[+] Setting GitMancer..."

cp gitmancerINS.sh $PREFIX/bin/bcbs upgrade
cp gitmancerRST.sh $PREFIX/bin/bcbs upgrade rst
cp gitmancerUPT.sh $PREFIX/bin/bcbs update



echo "[ OK ] Command installation finished"
echo "Type "bcbs" to inicializate BCBS-NetHunter"

hash -r
