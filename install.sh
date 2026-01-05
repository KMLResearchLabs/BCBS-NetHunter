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

mkdir -p $PREFIX/bin/bcbs-upgrade
cp gitmancerINS.sh $PREFIX/bin/bcbs-upgrade/
ln -s $PREFIX/bin/bcbs-upgrade/gitmancerINS.sh $PREFIX/bin/bcbs-upgrade
chmod +x $PREFIX/bin/bcbs-upgrade

mkdir -p $PREFIX/bin/bcbs-upforce
cp gitmancerRST.sh $PREFIX/bin/bcbs-upforce/
ln -s $PREFIX/bin/bcbs-upforce/gitmancerRST.sh $PREFIX/bin/bcbs-upforce
chmod +x $PREFIX/bin/bcbs-upforce

mkdir -p $PREFIX/bin/bcbs-update
cp gitmancerUPT.sh $PREFIX/bin/bcbs-update/
ln -s $PREFIX/bin/bcbs-update/gitmancerUPT.sh $PREFIX/bin/bcbs-update
chmod +x $PREFIX/bin/bcbs-update


echo "[ OK ] Command installation finished"
echo "Type "bcbs" to inicializate BCBS-NetHunter"

hash -r
