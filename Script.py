from colorama import Fore, Back, Style
from ast import If
from re import T
import subprocess
import os
import time
from urllib import response
import sys
import itertools


def loading_animation():
    animation = itertools.cycle(['-', '/', '|', '\\'])
    for i in range(50):
        sys.stdout.write(next(animation))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

try:
    subprocess.run("clear", shell=True)
    subprocess.run("tput setaf 2",shell=True)

    time.sleep(1)

    print("Launching Toolkit...")
    loading_animation()

    # sets the text color to red
    time.sleep(1)
    subprocess.run("tput setaf 1",shell=True)

    print("---------------------------------------------------------------")

    print("""/ /   ____ _ ____  __  __   / /_   ____ _ _____ / /__ _____
            / /   / __ `//_  / / / / /  / __ \ / __ `// ___// //_// ___/
           / /___/ /_/ /  / /_/ /_/ /  / / / // /_/ // /__ / ,<  (__  ) 
          /_____/\__,_/  /___/\__, /  /_/ /_/ \__,_/ \___//_/|_|/____/  
                            /____/                                      
                                                        """)           

    # sets the text color to white
    subprocess.run("tput setaf 7",shell=True)

    while True:
        print("      ------ TOOLS -------           ")
        print(Fore.YELLOW   + """ 
            1. Mac changer
            2. Log killer
            3. Managed mode
            4. Monitor mode
            5. Nmap scan
            6. Start Tor
            7. Stop tor
            8. Start whoami service
            9. Enable NetworkManager service
           10. Pentest-GPT
           11. Lazy script
           99. Exit """)

        ch=int(input("Enter your choice: ")) 
        loading_animation() 
        if ch == 1:
            subprocess.run("clear", shell=True)
            interface = input("Enter your Wireless Interface: ")
            time.sleep(2)
            subprocess.run("clear", shell=True)
            print("\t")
            loading_animation()
            print("  -----Options----")
            while True:
                print("""
                    1. Random Mac address
                    2. Custom Mac address
                    3. back""")
                ch=int(input("Enter your choice: "))

                if(ch == 1):
                    time.sleep(2)
                    subprocess.run("clear", shell=True)
                    print("\t")
                    print("Processing. . .")
                    loading_animation()
                    subprocess.run("ifconfig "+interface+" down",shell=True)
                    subprocess.run("macchanger -r "+ interface,shell=True)
                    subprocess.run("ifconfig "+interface+" up",shell=True)
                    print("\t")
                    print("done")
                    input("Press enter to continue")

                elif(ch == 2):
                    time.sleep(2)
                    subprocess.run("clear", shell=True)
                    print("\t")
                    mac = input("Enter Custom mac address: ")
                    loading_animation()
                    subprocess.run("ifconfig "+interface+" down", shell=True)
                    subprocess.run("ifconfig "+interface+" hw ether "+ mac, shell=True )
                    subprocess.run("ifconfig "+interface+" up", shell=True)
                    input("Press enter to continue")
                else:
                    break 

        elif ch == 2:
            time.sleep(2)
            subprocess.run("clear", shell=True)
            print("\t")
            response = input("Do you have log killer installed? (y/n): ")
            print("\t")
            if response == "n" or "N": 
                subprocess.run("git clone https://github.com/Rizer0/Log-killer.git ", shell=True)
                os.system("cd Log-killer")
                os.system("php cleartracks.php ")
            elif response == "y" or "Y":
                os.system("cd ~")
                os.system("cd Log-killer")
                os.system("php cleartracks.php ")

        elif ch == 3:
            subprocess.run("clear", shell=True)
            os.system("airmon-ng")
            interface = input("Enter your wireless interface: ")
            print("Enabling manage mode . . .")
            os.system("service Network-Manager start")
            os.system("service NetworkManger start")
            os.system("airmon-ng stop" + interface)
            print("Enabled Managed mode")
            break
    
        elif ch == 4:
            subprocess.run("clear", shell=True)
            interface = input("Enter your wireless interface  ")
            while True:
                print("""
                    1. Enable Monitor mode
                    2. Disable Monitor mode
                    3. View Selected Wireless Interface
                    4. Change Wireless Interface
                    5. back""")
                ch=int(input("Enter your choice: "))
                if ch == 1:
                    subprocess.run("clear", shell=True)
                    print("Enabling monitor mode. . .")
                    os.system("airmon-ng check kill")
                    subprocess.run("airmon-ng start" + interface, shell=True )
                    print("\t")
                    os.system("Monitor mode enabled")
                    print("\t")
                    input("Press Enter to Continue")
                elif ch==2:
                    subprocess.run("clear", shell=True)
                    print(" Disabling monitor mode. . .")
                    os.system("service NetworkManager start")
                    subprocess.run("airmon-ng stop" + interface, shell=True )
                    print("\t")
                    os.system("Monitor mode Disabled")
                    print("\t")
                    input("Press Enter to Continue")
                elif ch==3:
                    subprocess.run("clear", shell=True)
                    print("\t")
                    print(interface)
                    print("\t")
                    input("Press enter to Continue")
                    
                elif ch==4:
                    subprocess.run("clear", shell=True)
                    interface = input("Enter your wireless interface ")
                    print("\t")
                    input("Press Enter to Continue")
                        
                elif ch==5:
                    break    
                
                
        

        elif ch == 5:
            subprocess.run("clear", shell=True)
            target = input("Enter target IP or url: ")
            while True:
                print(Fore.RED + """    
                    Nmap scanner toolkit:

                    1. Scanning open ports
                    2. OS detection
                    3. Scan your network
                    4. Scan TCP or UDP protocols
                    5. Aggressive and obtrusive scan
                    6. Scan an IP address range
                    7. Default script scan
                    8. IP address information
                    9. Scan a firewall for MAC address spoofing
                    10. Scan filtered ports
                    11. Identify hostnames
                    12. Scan the most popular ports
                    13. Change target
                    14. View target
                    15. View Network gateway
                    99. back
                    """) 
                ch=int(input("Enter your choice: "))
                if(ch == 1):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap -Pn "+target+" > open-ports.txt",shell=True )
                    print("Scanned " + target)
                    input("Press enter to continue: ")

                elif(ch == 2):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap -O "+target+" > os-detection.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")

                elif(ch == 3):
                    subprocess.run("clear", shell=True)
                    gateway = input("Enter your network gateway(ex. 192.168.0.0/24): ")
                    subprocess.run("nmap -sS -O "+gateway+" > network-scan.txt",shell=True)
                    print("Full network scanned for " + gateway )
                    input("Press enter to continue: ")

                elif(ch == 4):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap -sT "+target+" > tcp-or-udp.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")

                elif(ch == 5):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap -T4 -A "+target+" > agressive-scan.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")


                elif(ch == 6):
                    subprocess.run("clear", shell=True)
                    range = input("Enter ip address range(ex. 192.168.1.100-110): ")
                    subprocess.run("nmap "+range+" > agressive-scan.txt",shell=True)
                    print("Scanned address range for " + range)
                    input("Press enter to continue: ")    


                elif(ch == 7):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap -sC "+target+" > default-script.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")

                elif(ch == 8):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap "+target+" --script whois-ip > ip-information.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")

                elif(ch == 9):
                    subprocess.run("clear", shell=True)
                    mac = input("Enter fake mac address of your choice: ")
                    subprocess.run("nmap -v -sT -PN --spoof-mac "+mac+" "+target+" > Mac-spoofing.txt",shell=True )
                    print("Scanned " + target)
                    input("Press enter to continue: ")


                elif(ch == 10):
                    subprocess.run("clear", shell=True)
                    port = int("Enter a ports(80,22): ")
                    subprocess.run("nmap -sA -p "+port+" "+target+" > filtered-ports.txt",shell=True)
                    print("Scanned " + target +" > with port "+port  )
                    input("Press enter to continue: ")


                elif(ch == 11):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap -sL "+target+" > hostnames.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")

                elif(ch == 12):
                    subprocess.run("clear", shell=True)
                    subprocess.run("nmap --top-ports 20 "+target+" > most-popular-ports.txt",shell=True)
                    print("Scanned " + target)
                    input("Press enter to continue: ")


                elif(ch == 13):
                    subprocess.run("clear", shell=True)
                    target = input("Enter target IP or url again: ")
                    input("Press enter to continue")
                elif(ch == 14):
                    subprocess.run("clear", shell=True)
                    print("Current target "+target)
                    input("Press enter to continue")
            
                elif(ch == 15):
                    subprocess.run("clear", shell=True)
                    print(gateway)
                    input("Press enter to continue")
                elif(ch == 99):
                    time.sleep(1)
                    break
            
        elif ch == 6:
            subprocess.run("clear", shell=True)
            print("STARTING tor service. . .")
            subprocess.run("service tor start",shell=True)
            input("Press enter to continue")
    
        elif ch == 7:
            subprocess.run("clear", shell=True)
            print("Stoping tor service . . .")
            subprocess.run("service tor stop",shell=True)
                
        elif ch == 8:
            if ch == 8:
                time.sleep(1)
                subprocess.run("clear", shell=True)
                print("\t")
        
                # Checking if WHOAMI is installed
                try:
                    result = subprocess.run("which kali-whoami", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                    if result.returncode == 0:
                        print("WHOAMI is already installed.")
                    else:
                        print("Kali-WHoami is not installed ")    
                except subprocess.CalledProcessError:
                    print("Error occurred while checking KALI-WHOAMI.")
                    print("\t")
            
                response = input("Do you like to install kali-WHOAMI? (y/n): ")
                print("\t")
            
                if response == "y":
                    subprocess.run("clear", shell=True) 
                    print("Downloading and Installing WHOAMI . . .")
                    print("\t")
                    os.system("sudo apt-get update && sudo apt install tar tor curl python3 python3-scapy network-manager")
                    subprocess.run("git clone https://github.com/owerdogan/whoami-project ", shell=True)
                    os.system("cd whoami-project ")
                    os.system("sudo make install ")
                    print("\t")
                    print("Installed")
                    input("Press enter to continue: ")
        
                elif response == "n":
                    subprocess.run("clear", shell=True)
                    print("Launching whoami . . .")
                    while True:
                        print(""" Options
                                1. Start
                                2. Stop
                                3. Status
                                4. Fix
                                5. Help
                                6. back""")
                        ch=int(input("Enter your choice: "))
                        if ch==1:
                            subprocess.run("clear", shell=True)
                            print("\t")
                            loading_animation()
                            print("Starting WHOAMI . . . ")
                            time.sleep(1)
                            os.system("sudo kali-whomai --start")
                            input("Press enter to continue")
                            
except Exception as e:
    print(f"An error occurred: {e}")
       



 
    
