def banner():
    print("""

########################################
##                                    ##
##  ██████╗  ██████╗██████╗ ███████╗  ##
##  ██╔══██╗██╔════╝██╔══██╗██╔════╝  ##
##  ██████╔╝██║     ██████╔╝███████╗  ##
##  ██╔══██╗██║     ██╔══██╗╚════██║  ##
##  ██████╔╝╚██████╗██████╔╝███████║  ##
##  ╚═════╝  ╚═════╝╚═════╝ ╚══════╝  ##
##                                    ##
############## NetHunter ###############

        <By KML Research Labs>
""")

def get_version():
    print("==== <System Version> ====")
    print("[+] BLKCR Net Version: 2.3")
    print("[+] BCBS Version: 2.0")
    print("[+] GitMancer Version: 1.4")
    print("[+] Developer: ByKurebo")

def clear():
    import os
    os.system('clear')

def exit():
    import os
    os.system('exit()')

# User configs

def user_configs():
    with open("userconfigs.txt", "r") as f:
        content = f.read()
        print(" ")
        print(content)

def get_user():
    username = ""
    with open("userconfigs.txt", "r") as f:
        for line in f:
            if "%User%" in line:
                username = line.strip()
                break
    username_final = username.split(":")
    terminaluser = username_final[1]
    return terminaluser

def user_configs_USER():
    new_user = []
    newuser = str(input("\n>>> Type the new username: "))

    confirmation = str(input("\nConfirm this action? [Y/n]: ")).strip().lower()
    if confirmation == "y":
        with open("userconfigs.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("%User%"):
                    new_user.append(f"%User%:{newuser}\n")
                else:
                    new_user.append(line)

        with open("userconfigs.txt", "w", encoding="utf-8") as f:
            f.writelines(new_user)
        print(f"\n[ OK ] Username changed to {newuser}")
    else:
        print("\n[!] Action canceled by user")


