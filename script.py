#!/user/bin/python

import socket
from colorama import Fore, init


class Scan:
    # colors to customize
    init(autoreset=True)

    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUES = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

    def ScaningPort(ip = str, mode = str):
        COMMONPORTSTCP = [20, 21, 22,23,25,563,80,110,143,445,993,995,1433,1521,3306,3389,5900,8080]
        modes = ["hard", "easy"]
        openport = []

        if mode  == modes[0]:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockTCP:
                sockTCP.settimeout(1) 
                for port in range(0, 65535):
                    coneted = sockTCP.connect_ex((ip, port))
                    if coneted == 0:
                        print(Scan.GREEN + f"Port {port} Open [TCP]")
                        openport.append(port)
                if len(openport) == 0:
                    print(Scan.RED + "No open ports found")
                sockTCP.close()

        if mode == modes[1]:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockTCP:
                sockTCP.settimeout(1) 
                for port in COMMONPORTSTCP:
                    coneted = sockTCP.connect_ex((ip, port))
                    if coneted == 0:
                        print(Scan.GREEN + f"Port {port} Open [TCP]")
                        openport.append(port)
                if len(openport) == 0:
                     print(Scan.RED + "No open ports found")
                sockTCP.close()


if __name__ == "__main__":

    print(Scan.MAGENTA + "Select the scan mode")
    print(Scan.CYAN + "[MODE       DESCRIPTION]")
    print(Scan.CYAN + "easy    Common port scanning")
    print(Scan.CYAN + "hard    Scanning all ports\n")

    try:
        mode = input(Scan.WHITE + "[MODE]@> ")
        ip = input(Scan.WHITE + "[DESTINATION IP]@> ")
        Scan.ScaningPort(ip = ip, mode = mode)
    except KeyboardInterrupt:
        print(Scan.RED + "\nexit\n")
