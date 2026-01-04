# BCBS-NetHunter  
The NetHunter for Termux, but with the KML and BCBS touch  

Kali NetHunter in Termux is a great code, so inspired on it, KML Research Labs released BCBS NetHunter: a cybertool that can track  
IP's, make WHOIS consults, and etc. For now the system is in development phase, but, you can get an idea of what it is. Cheers!   

  
### **1. How to install BCBS NetHunter**

First you need to have Termux installed on your device, make this searching on Play Store for "Termux".
Now enter on Termux and in the terminal command line type these folloowing commands (Confirm any action
that the program ask to you):

1. pkg upgrade
2. pkg install python
3. pkg install git
4. pip install colorama

Now you have Termux in the latest version with Python and Git. To get BCBS, clone the repo using:

1. git clone https://github.com/KMLResearchLabs/BCBS-NetHunter.git

Now you have BCBS NetHunter

  
### **2. How to start the system**

In the Termux terminal type:

1. ls

And check if "BCBS NetHunter" appeared in purple on the terminal (If not check the page "How to install BCBS NetHunter").
Now to acess type this following commands:

1. cd BCBS-NetHunter
2. cd 'BLKCR Net'
3. python terminal.py

Now you acessed BCBS
But you can also configure the launcher:

1. cd BCBS-NetHunter
2. chmod +x bcbslauncher.sh
3. ./bcbslauncher.sh
(Note: use commands 1 and 3 to acess)

Or...
You can asign a command in Termux (this is my favorite):

1. cd BCBS-NetHunter
2. chmod +x install.sh
3. ./install.sh
4. cd ..
5. bcbs

So now to acess just type "bcbs" on Termux command line

  
### **3. First usage**

First you need to update system libs and files, so on the command line type:

1. update

This you take a little longer, but wait. And in the final the system will ask if you want to restart, confirm typing "y" and enter.
After type:

1. python terminal.py

But if somehow you missed the confirmantion, on the command line type:

1. exit
2. python terminal.py

Now to see your user configs type:  

1. userc

To change your username, type

1. userc -u

Type your new username, and after confirm the action.  

  
Terminal commands:  
help - Show the commands              
clear - Clean the terminal
exit - Exit the system
version - Show the system version
update - Check for updates
userc - Get user configs
userc -u - Change username
userc -t - Change sys theme
blckport - Makes a portscan on domains
geop - Consult phone (Only BR for now)
ip -lcz - Track ip's
ip -dmn - Get domains ip
ip -whs - Make WHOIS consult  
