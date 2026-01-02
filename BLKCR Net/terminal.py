from terminal_package import *
from gitmancer import *
from terminal_commands.blackport import *
from terminal_commands.geo_phone import *
from terminal_commands.ip_log import *

banner()

while True:
    print("\n/[ByKurebo@BCBS]~<Root>")
    cmd = str(input(r"\> ")).strip()

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

    if cmd == "version":
        get_version()


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

    if cmd == "update":
        gitmancer()
    
    if cmd == "test":
        print("[ OK ]")
        