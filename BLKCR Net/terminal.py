from terminal_package import *
from gitmancer import *
from terminal_commands.blackport import *
from terminal_commands.geo_phone import *
from terminal_commands.ip_log import *

banner()

while True:
    user = get_user()
    print(f"\n/[{user}@BCBS]~<Root>")
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
        banner()

    if cmd == "exit":
        exit()
        break

    if cmd == "version":
        get_version()

    if cmd == "update":
        gitmancer()
        print("\n [!] If there something updated, confirm to restart the system.")
        restart = str(input("\n Restart now? [y/n]: ")).strip().lower()
        if restart == "y":
            exit()
            break
        else:
            print("\n [!] Restart cancelled by user.")
       

    if cmd == "userc":
        user_configs()

    if cmd == "userc -u":
        user_configs_USER()


    if cmd == "blckport":
        blackport()

    if cmd == "geop":
        geo_phone_br()

    if cmd == "ip -lcz":
        geo_IP()

    if cmd == "ip -dmn":
        get_domain_ip()

    if cmd == "ip -whs":
        get_domain_whois()
