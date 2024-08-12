# BlueStorm
A tool which perform deauthentication attack on unpaired bluetooth devices.

# Meaning of Unpaired devices
Those bluetooth devices which is paired but going to connect.

# Screenshot
![BlueStorm](https://github.com/user-attachments/assets/095b710f-c6bb-49c3-b4b5-33ba74fd54f5)

# OS Support
- Kali Linux
- Raspberry Pi OS

# Setup
Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).

# Install and Run
1. Run the following command to start terminal in root :
```
sudo su -
```
2. Run the following command to check bluetooth interfaces, BUS and its running status on your system :
```
hciconfig
```
- Check Interface, Bus and Running Status.
- Interface look like `hciX`.
- `X` is a number starts from 0 like `hci0`, `hci1` *etc.*.
- There are two types : `UART` and `USB`.
- `UART` is buit-in Bluetooth Interface and `USB` is external Bluetooth Interface like Adapter.
- There are commanly two types of Running Status : `DOWN` and `UP RUNNING`.
- `DOWN` means the interface is `OFF` and `UP RUNNING` means the interface is `ON`. 
3. Run the following command to start bluetooth interface if it is not started :
```
hciconfig hciX up
```
4. Run the following command to scan nearby bluetooth devices and store in a `.txt` file for future use :
```
hcitool -i hciX scan > scaned_devices.txt
```
4. Download or Clone the Repository.
5. Open the folder and run the *BlueStorm.py* file by type the following command :
```
python3 BlueStorm.py
```
6. Enter the following particulars :
   1. Bluetooth Interface
   2. Target MAC Address
   3. Packet Size
   4. Number of threads
7. `Packet Size` must be less than or equal to `600` and `Number of threads` must be less than or equal to `1200`.
8. After that, press Enter.
9. Done!

# What happened after execution of script?
1. If bluetooth device is going to connect, it is not able to connect.
2. If it is connected, then the slight disturbance is happening during listing music or watching videos.<br>
It takes some time to happen disturbance.<br>
It is like someone is pause and play quickly in few seconds.<br>
The disturbance is not much powerful but it is enough to irritate.

# For Better Results
- Use a Bluetooth Adapter for better results of the tool.
- Make sure that Bluetooth Adapter supports `HCI` mode.
- **TP-Link UB400 USB Bluetooth Adapter** is one of the Bluetooth Adapter.
- Bluetooth adapter that has `CSR8510 A10` is good.
- If bluetooth adapter has a long range dBi antenna, then it is very good and most effective for deauth attack.
- To check Bluetooth Adapter supports HCI mode or not, there are two ways :
  1. Type `lsusb` command after connecting adapter to the system.
     - It show the `(HCI Mode)` at the end of the adapter name means it supports HCI mode.
  2. Type `hciconfig hciX up`.
     - If it is up then it supports HCI mode, otherwise not.

# Warning
- Some cheap Bluetooth Adapters show that it supports HCI mode but it does not work.
- Some cheap Bluetooth Adapters works on only one OS but not on other OS.
- Some cheap Bluetooth Adapters does not support Linux.
