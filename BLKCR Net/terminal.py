from colorama import init, Fore, Style
from terminal_package import *
from gitmancer import *
from terminal_commands.blackport import *
from terminal_commands.geo_phone import *
from terminal_commands.ip_log import *

init()
clear()
theme_banner()

while True:
    colors = theme()
    user = get_user()
    print(f"\n/[{colors['%USR%']}{user}@BCBS{colors['%---%']}]{colors['%~~~%']}~{colors['%---%']}<{colors['%ROT%']}Root{colors['%---%']}>")
    cmd = str(input(r"\> ")).strip().lower()


    ############
    # COMMANDS #
    ############

    if cmd == "help":
        print("""
========= <COMMANDS> =========
help - Show the commands              
clear - Clean the terminal
exit - Exit the system
version - Show the system version
update - Check for updates
userc - Get user configs
userc -u - Change username
blckport - Makes a portscan on domains
geop - Consult phone (Only BR for now)
ip -lcz - Track ip's
ip -dmn - Get domains ip
ip -whs - Make WHOIS consult 
""")

    if cmd == "clear":
        clear()
        theme_banner()

    if cmd == "exit":
        exit()
        break

    if cmd == "version":
        get_version(colors)

    if cmd == "update":
        gitmancer(colors)
        print(f"\n [{colors["%>!<%"]}!{colors["%---%"]}] Restart required to apply updates")
        restart = str(input("\n Restart now? [y/n]: ")).strip().lower()
        if restart == "y":
            exit()
            break
        else:
            print(f"\n [{colors["%>!<%"]}!{colors["%---%"]}] Restart cancelled by user.")
       

    if cmd == "userc":
        user_configs()

    if cmd == "userc -u":
        user_configs_USER(colors)

    if cmd == "userc -t":
        user_configs_THEME(colors)


    if cmd == "blckport":
        blackport(colors)

    if cmd == "geop":
        geo_phone_br(colors)

    if cmd == "ip -lcz":
        geo_IP(colors)

    if cmd == "ip -dmn":
        get_domain_ip(colors)

    if cmd == "ip -whs":
        get_domain_whois(colors)
