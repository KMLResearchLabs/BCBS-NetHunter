def banner(dual, colors):
    if dual == False:
        print(f"""
{colors['%<1>%']}
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
        
    if dual == True:
        print(f"""
{colors['%<1>%']}
########################################
##                                    ##
##{colors['%<2>%']}  ██████╗  ██████╗██████╗ ███████╗  {colors['%<1>%']}##
##{colors['%<2>%']}  ██╔══██╗██╔════╝██╔══██╗██╔════╝  {colors['%<1>%']}##
##{colors['%<2>%']}  ██████╔╝██║     ██████╔╝███████╗  {colors['%<1>%']}##
##{colors['%<2>%']}  ██╔══██╗██║     ██╔══██╗╚════██║  {colors['%<1>%']}##
##{colors['%<2>%']}  ██████╔╝╚██████╗██████╔╝███████║  {colors['%<1>%']}##
##{colors['%<2>%']}  ╚═════╝  ╚═════╝╚═════╝ ╚══════╝  {colors['%<1>%']}##
##                                    ##
############## {colors['%<2>%']}NetHunter {colors['%<1>%']}###############

        <{colors['%<2>%']}By KML Research Labs{colors['%<1>%']}>
""")

def get_version(colors):
    print(" ==== <System Version> ====")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] BLKCR Net Version: 2.3")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] BCBS Version: 2.0")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] GitMancer Version: 1.4")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Developer: ByKurebo")

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

def user_configs_USER(colors):
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
        print(f"\n[{colors["%>K<%"]} OK {colors["%---%"]}] Username changed to {newuser}")
    else:
        print(f"\n[{colors["%>!<%"]}!{colors["%---%"]}] Action canceled by user")


def get_theme():
    theme = ""
    with open("userconfigs.txt", "r") as f:
        for line in f:
            if "%Theme%" in line:
                theme = line.strip()
                break
    theme_final = theme.split(":")
    terminaltheme = theme_final[1]
    return terminaltheme

def user_configs_THEME(colors):
    themes = ["1", "2", "3"]
    new_theme = []
    print("\n[1] Mono [2] Carnival [3] IceFrost")
    while True:
        newtheme = str(input("\n>>> Select the theme number: "))
        if newtheme in themes:
            break
        else:
            print(f" [{colors["%>!<%"]}!{colors["%---%"]}] Select a valid theme number")

    if newtheme == "1":
        newtheme = "Mono"
    if newtheme == "2":
        newtheme = "Carnival"
    if newtheme == "3":
        newtheme = "IceFrost"

    confirmation = str(input("\nConfirm this action? [Y/n]: ")).strip().lower()
    if confirmation == "y":
        with open("userconfigs.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("%Theme%"):
                    new_theme.append(f"%Theme%:{newtheme}\n")
                else:
                    new_theme.append(line)

        with open("userconfigs.txt", "w", encoding="utf-8") as f:
            f.writelines(new_theme)
        print(f"\n[{colors["%>K<%"]} OK {colors["%---%"]}] Theme changed to {newtheme}")
    else:
        print(f"\n[{colors["%>!<%"]}!{colors["%---%"]}] Action canceled by user")

def theme():
    from colorama import Fore, Style
    selected_theme = get_theme()
    themes = {
        "Mono": {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%>+<%":Fore.LIGHTWHITE_EX, #[+]
            "%>-<%":Fore.LIGHTWHITE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTWHITE_EX, # [ OK ]
            "%>!<%":Fore.LIGHTWHITE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTWHITE_EX, # <Root>
            "%~~~%":Fore.LIGHTWHITE_EX, # ~
            "%USR%":Fore.LIGHTWHITE_EX, # [User@BCBS]
            "%---%":Style.RESET_ALL # RESET
        },
    
        "Carnival": {
            "%<1>%":Fore.LIGHTMAGENTA_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%>+<%":Fore.LIGHTGREEN_EX, #[+]
            "%>-<%":Fore.LIGHTRED_EX, # [ERROR]
            "%>K<%":Fore.LIGHTGREEN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTYELLOW_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTYELLOW_EX, # [User@BCBS]
            "%---%":Style.RESET_ALL # RESET
        },
    

        "IceFrost": {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTCYAN_EX, # Second sys color
            "%>+<%":Fore.LIGHTCYAN_EX, # [+]
            "%>-<%":Fore.LIGHTBLUE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTCYAN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTBLUE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTCYAN_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTBLUE_EX, # [User@BCBS]
            "%---%":Style.RESET_ALL # RESET
        }
    }
    return themes.get(selected_theme, themes["Mono"])

    
def theme_banner():
    from colorama import Fore, Style
    theme = get_theme()
    if theme == "Mono":
        colors = {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%>+<%":Fore.LIGHTWHITE_EX, #[+]
            "%>-<%":Fore.LIGHTWHITE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTWHITE_EX, # [ OK ]
            "%>!<%":Fore.LIGHTWHITE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTWHITE_EX, # <Root>
            "%~~~%":Fore.LIGHTWHITE_EX, # ~
            "%USR%":Fore.LIGHTWHITE_EX, # [User@BCBS]
            "%---%":Style.RESET_ALL # RESET
        }
        banner(False, colors)
        print(colors["%---%"])
        return colors

    if theme == "Carnival":
        colors = {
            "%<1>%":Fore.LIGHTMAGENTA_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%>+<%":Fore.LIGHTGREEN_EX, #[+]
            "%>-<%":Fore.LIGHTRED_EX, # [ERROR]
            "%>K<%":Fore.LIGHTGREEN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTYELLOW_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTYELLOW_EX, # [User@BCBS]
            "%---%":Style.RESET_ALL # RESET
        }
        banner(True, colors)
        print(colors["%---%"])
        return colors

    if theme == "IceFrost":
        colors = {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTCYAN_EX, # Second sys color
            "%>+<%":Fore.LIGHTCYAN_EX, # [+]
            "%>-<%":Fore.LIGHTBLUE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTCYAN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTBLUE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTCYAN_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTBLUE_EX, # [User@BCBS]
            "%---%":Style.RESET_ALL # RESET
        }
        banner(True, colors)
        print(colors["%---%"])
        return colors