def banner(dual, colors):
    if dual == "%Uno%":
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
        
    if dual == "%Duo%":
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
        
    if dual == '%Triple%':
        print(f"""
{colors['%<1>%']}
########################################
##                                    ##
##{colors['%<2>%']}  ██████{colors['%<3>%']}╗{colors['%<2>%']}  ██████{colors['%<3>%']}╗{colors['%<2>%']}██████{colors['%<3>%']}╗{colors['%<2>%']} ███████{colors['%<3>%']}╗{colors['%<2>%']}  {colors['%<1>%']}##
##{colors['%<2>%']}  ██{colors['%<3>%']}╔══{colors['%<2>%']}██{colors['%<3>%']}╗{colors['%<2>%']}██{colors['%<3>%']}╔════╝{colors['%<2>%']}██{colors['%<3>%']}╔══{colors['%<2>%']}██{colors['%<3>%']}╗{colors['%<2>%']}██{colors['%<3>%']}╔════╝ {colors['%<1>%']} ##
##{colors['%<2>%']}  ██████{colors['%<3>%']}╔╝{colors['%<2>%']}██{colors['%<3>%']}║{colors['%<2>%']}     ██████{colors['%<3>%']}╔╝{colors['%<2>%']}███████{colors['%<3>%']}╗  {colors['%<1>%']}##
##{colors['%<2>%']}  ██{colors['%<3>%']}╔══{colors['%<2>%']}██{colors['%<3>%']}╗{colors['%<2>%']}██{colors['%<3>%']}║     {colors['%<2>%']}██{colors['%<3>%']}╔══{colors['%<2>%']}██{colors['%<3>%']}╗╚════{colors['%<2>%']}██{colors['%<3>%']}║  {colors['%<1>%']}##
##{colors['%<2>%']}  ██████{colors['%<3>%']}╔╝╚{colors['%<2>%']}██████{colors['%<3>%']}╗{colors['%<2>%']}██████{colors['%<3>%']}╔╝{colors['%<2>%']}███████{colors['%<3>%']}║  {colors['%<1>%']}##
##{colors['%<2>%']}  {colors['%<3>%']}╚═════╝  ╚═════╝╚═════╝ ╚══════╝  {colors['%<1>%']}##
##                                    ##
############## {colors['%<2>%']}NetHunter {colors['%<1>%']}###############

        <{colors['%<2>%']}By KML Research Labs{colors['%<1>%']}>
""")

def get_version(colors):
    print(f"\n==== <{colors['%<2>%']}System Version{colors['%---%']}> ====")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] BLKCR Net Version: {colors["%>§<%"]}2.7{colors["%---%"]}")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] BCBS Version: {colors["%>§<%"]}2.5{colors["%---%"]}")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] GitMancer Version: {colors["%>§<%"]}1.9{colors["%---%"]}")
    print(f"[{colors["%>+<%"]}+{colors["%---%"]}] Developer: {colors["%>§<%"]}ByKurebo{colors["%---%"]}")

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
    themes = ["1", "2", "3", "4", "5"]
    new_theme = []
    print("\n[1] Default [2] Mono [3] Carnival [4] IceFrost [5] Magma")
    while True:
        newtheme = str(input("\n>>> Select the theme number: "))
        if newtheme in themes:
            break
        else:
            print(f"[{colors["%>!<%"]}!{colors["%---%"]}] Select a valid theme number")

    if newtheme == "1":
        newtheme = "Default"
    if newtheme == "2":
        newtheme = "Mono"
    if newtheme == "3":
        newtheme = "Carnival"
    if newtheme == "4":
        newtheme = "IceFrost"
    if newtheme == "5":
        newtheme = "Magma"

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
        "Default": {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTMAGENTA_EX, # Second sys color
            "%<3>%":Fore.MAGENTA, # Third color
            "%>+<%":Fore.LIGHTGREEN_EX, #[+]
            "%>-<%":Fore.LIGHTRED_EX, # [ERROR]
            "%>K<%":Fore.LIGHTGREEN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTGREEN_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTWHITE_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTYELLOW_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        },

        "Mono": {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%<3>%":Fore.LIGHTWHITE_EX, # Third color
            "%>+<%":Fore.LIGHTWHITE_EX, #[+]
            "%>-<%":Fore.LIGHTWHITE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTWHITE_EX, # [ OK ]
            "%>!<%":Fore.LIGHTWHITE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTWHITE_EX, # <Root>
            "%~~~%":Fore.LIGHTWHITE_EX, # ~
            "%USR%":Fore.LIGHTWHITE_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTWHITE_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        },
    
        "Carnival": {
            "%<1>%":Fore.LIGHTMAGENTA_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%<3>%":Fore.LIGHTWHITE_EX, # Third color
            "%>+<%":Fore.LIGHTGREEN_EX, #[+]
            "%>-<%":Fore.LIGHTRED_EX, # [ERROR]
            "%>K<%":Fore.LIGHTGREEN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTYELLOW_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTYELLOW_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTYELLOW_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        },
    

        "IceFrost": {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTCYAN_EX, # Second sys color
            "%<3>%":Fore.BLUE, # Third color
            "%>+<%":Fore.LIGHTCYAN_EX, # [+]
            "%>-<%":Fore.LIGHTBLUE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTCYAN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTBLUE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTCYAN_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTBLUE_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTCYAN_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        },

        "Magma": {
            "%<1>%":Fore.BLACK, # Primarly sys color
            "%<2>%":Fore.LIGHTRED_EX, # Second sys color
            "%<3>%":Fore.RED, # Third color
            "%>+<%":Fore.LIGHTRED_EX, # [+]
            "%>-<%":Fore.RED, # [ERROR]
            "%>K<%":Fore.LIGHTRED_EX, # [ OK ]
            "%>!<%":Fore.LIGHTRED_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.RED, # [User@BCBS]
            "%>§<%":Fore.LIGHTRED_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        }
    }
    return themes.get(selected_theme, themes["Default"])

    
def theme_banner():
    from colorama import Fore, Style
    theme = get_theme()
    if theme == "Default":
        colors = {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTMAGENTA_EX, # Second sys color
            "%<3>%":Fore.MAGENTA, # Third color
            "%>+<%":Fore.LIGHTGREEN_EX, #[+]
            "%>-<%":Fore.LIGHTRED_EX, # [ERROR]
            "%>K<%":Fore.LIGHTGREEN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTGREEN_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTWHITE_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTYELLOW_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        }
        banner("%Triple%", colors)
        print(colors["%---%"])
        return colors

    if theme == "Mono":
        colors = {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%<3>%":Fore.LIGHTWHITE_EX, # Third color
            "%>+<%":Fore.LIGHTWHITE_EX, #[+]
            "%>-<%":Fore.LIGHTWHITE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTWHITE_EX, # [ OK ]
            "%>!<%":Fore.LIGHTWHITE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTWHITE_EX, # <Root>
            "%~~~%":Fore.LIGHTWHITE_EX, # ~
            "%USR%":Fore.LIGHTWHITE_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTWHITE_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        }
        banner("%Uno%", colors)
        print(colors["%---%"])
        return colors

    if theme == "Carnival":
        colors = {
            "%<1>%":Fore.LIGHTMAGENTA_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTWHITE_EX, # Second sys color
            "%<3>%":Fore.LIGHTWHITE_EX, # Third color
            "%>+<%":Fore.LIGHTGREEN_EX, #[+]
            "%>-<%":Fore.LIGHTRED_EX, # [ERROR]
            "%>K<%":Fore.LIGHTGREEN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTYELLOW_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTYELLOW_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTYELLOW_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        }
        banner("%Duo%", colors)
        print(colors["%---%"])
        return colors

    if theme == "IceFrost":
        colors = {
            "%<1>%":Fore.LIGHTWHITE_EX, # Primarly sys color
            "%<2>%":Fore.LIGHTCYAN_EX, # Second sys color
            "%<3>%":Fore.BLUE, # Third color
            "%>+<%":Fore.LIGHTCYAN_EX, # [+]
            "%>-<%":Fore.LIGHTBLUE_EX, # [ERROR]
            "%>K<%":Fore.LIGHTCYAN_EX, # [ OK ]
            "%>!<%":Fore.LIGHTBLUE_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTCYAN_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.LIGHTBLUE_EX, # [User@BCBS]
            "%>§<%":Fore.LIGHTCYAN_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        }
        banner("%Triple%", colors)
        print(colors["%---%"])
        return colors
    
    if theme == "Magma":
        colors = {
            "%<1>%":Fore.BLACK, # Primarly sys color
            "%<2>%":Fore.LIGHTRED_EX, # Second sys color
            "%<3>%":Fore.RED, # Third color
            "%>+<%":Fore.LIGHTRED_EX, # [+]
            "%>-<%":Fore.RED, # [ERROR]
            "%>K<%":Fore.LIGHTRED_EX, # [ OK ]
            "%>!<%":Fore.LIGHTRED_EX, # [!]/[<>]
            "%ROT%":Fore.LIGHTRED_EX, # <Root>
            "%~~~%":Fore.LIGHTGREEN_EX, # ~
            "%USR%":Fore.RED, # [User@BCBS]
            "%>§<%":Fore.LIGHTRED_EX, # ByKurebo
            "%---%":Style.RESET_ALL # RESET
        }
        banner("%Triple%", colors)
        print(colors["%---%"])
        return colors
    
def theme_show(colors):
    user = get_user()
    print(f"""\n
==== <DEMONSTRATION> ====
{colors["%<1>%"]}111{colors["%---%"]} - %<1>%
{colors["%<2>%"]}222{colors["%---%"]} - %<2>%
{colors["%<3>%"]}333{colors["%---%"]} - %<3>%
[{colors["%>+<%"]}+{colors["%---%"]}] - %>+<%
[{colors["%>-<%"]}ERROR{colors["%---%"]}] - %>-<%
[ {colors["%>K<%"]}OK{colors["%---%"]} ] - %>K<%
[{colors["%>!<%"]}<>{colors["%---%"]}] - %>!<%
[{colors["%>!<%"]}!{colors["%---%"]}] - %>!<%
<{colors["%ROT%"]}Root{colors["%---%"]}> - %ROT%
{colors["%~~~%"]}~{colors["%---%"]} - %~~~%
[{colors["%USR%"]}{user}@BCBS{colors["%---%"]}] - %USR%
{colors["%>§<%"]}ByKurebo{colors["%---%"]} - %>§<%
""")