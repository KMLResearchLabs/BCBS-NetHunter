# BCBS-NetHunter  
The NetHunter for Termux, but with the KML and BCBS touch  

Kali NetHunter in Termux is a great code, so inspired on it, KML Research Labs released BCBS NetHunter: a cybertool that can track  
IP's, make WHOIS consults, and etc. For now the system is in development phase, but, you can get an idea of what it is. Cheers!   

  
### **1. How to install BCBS NetHunter**

First you need to have Termux installed on your device, make this searching on Play Store for "Termux".
Now enter on Termux and in the terminal command line type these folloowing commands (Confirm any action
that the program ask to you):

1. pkg upgrade
2. pkg install git

Now you have Termux in the latest version and Git. To get BCBS, clone the repo using:

1. git clone https://github.com/KMLResearchLabs/BCBS-NetHunter.git

Now you have BCBS NetHunter archives.

To install type:

1. cd BCBS-NetHunter
2. chmod +x install.sh
3. ./install.sh

Now you got the system and commands.
  
### **2. How to start and update/upgrade the system**

To acess BCBS, in the Termux terminal type:

1. bcbs
 
But before i recommend to first run:

1. bcbs update

And after:

1. bcbs upgrade

If the system don't run after run "bcbs upgrade", run:

1. bcbs upgrade reset

(Note: i recommend using this in place of "bcbs upgrade", the only bad
thing is that your user configs are reseted.)

  
### **3. First usage**

Now to see your user configs type:  

1. userc

To change your username, type:

1. userc -u

To change the theme:

1. userc -t

Type your new username, and after confirm the action.  

Termux commands:
bcbs - Acess BCBS
bcbs-UPT - Check for updates
bcbs-INS - Upgrade the system
bcbs-RST - More secure upgrade
  
Terminal commands:  
help - Show the commands              
clear - Clean the terminal
exit - Exit the system
version - Show the system version
update - Check for updates
userc - Get user configs
userc -u - Change username
userc -t - Change sys theme
userc -ts - Demonstrate the theme
blckport - Makes a portscan on domains
geop - Consult phone (Only BR for now)
ip -lcz - Track ip's
ip -dmn - Get domains ip
ip -whs - Make WHOIS consult  
