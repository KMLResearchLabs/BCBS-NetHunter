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
        print(f"""
========= <{colors['%<2>%']}COMMANDS{colors['%---%']}> =========
{colors['%>§<%']}help{colors['%---%']} - Show the commands              
{colors['%>§<%']}clear{colors['%---%']} - Clean the terminal
{colors['%>§<%']}exit{colors['%---%']} - Exit the system
{colors['%>§<%']}version{colors['%---%']} - Show the system version
{colors['%>§<%']}update{colors['%---%']} - Check for updates
{colors['%>§<%']}userc{colors['%---%']} - Get user configs
{colors['%>§<%']}userc -u{colors['%---%']} - Change username
{colors['%>§<%']}userc -t{colors['%---%']} - Change sys theme
{colors['%>§<%']}userc -ts{colors['%---%']} - Demonstrate the theme
{colors['%>§<%']}blckport{colors['%---%']} - Makes a portscan on domains
{colors['%>§<%']}geop{colors['%---%']} - Consult phone (Only BR for now)
{colors['%>§<%']}ip -lcz{colors['%---%']} - Track ip's
{colors['%>§<%']}ip -dmn{colors['%---%']} - Get domains ip
{colors['%>§<%']}ip -whs{colors['%---%']} - Make WHOIS consult 
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
       

    if cmd == "userc":
        user_configs()

    if cmd == "userc -u":
        user_configs_USER(colors)

    if cmd == "userc -t":
        user_configs_THEME(colors)

    if cmd == "userc -ts":
        theme_show(colors)


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

