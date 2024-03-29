# BlueStorm
A tool which perform deauthentication attack on unpaired bluetooth devices.

# Meaning of Unpaired devices
Those bluetooth devices which is paired but going to connect.

# Key Features
- Simple and clean menu.
- Support keyboard interrupts.
- Show scanned bluetooth devices in a borderless table.
- Show bluetooth interfaces and its status and select to use that interface.
- Simple and clean interface for deauthentication attack on target device.

# OS Support
- Kali Linux
- Raspberry Pi OS

# Setup
Make sure the latest python and pip3 is installed on your system (Windows/Linux/MacOS).

# Install and Run
## 1. Run the following command to start terminal in root :
   ```
   sudo su -
   ```
## 2. Run the following command to check bluetooth interfaces, BUS and its running status on your system :
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
## 3. Run the following command to start bluetooth interface if it is not started :
   ```
   hciconfig hciX up
   ```
## 4. Download or Clone the Repository.<br>
## 5. Open the folder and run the *BlueStorm.py* file by type the following command :
```
python3 BlueStorm.py
```
# For Better Results
- Use a Bluetooth Adapter for better results of the tool.
- Make sure that Bluetooth Adapter supports `HCI` mode.
- **TP-Link UB400 USB Bluetooth Adapter** is one of the Bluetooth Adapter.
- To check Bluetooth Adapter supports HCI mode or not, there are two ways :
  1. Type `lsusb` command after connecting adapter to the system.
     - It show the `(HCI Mode)` at the end of the adapter name means it supports HCI mode.
  2. Type `hciconfig hciX up`.
     - If it is up then it supports HCI mode, otherwise not.

# Warning
- Some cheap Bluetooth Adapters show that it supports HCI mode but it does not work.
- Some cheap Bluetooth Adapters works on only one OS but not on other OS.
- Some cheap Bluetooth Adapters does not support Linux.

# Some Comman Errors
1. `Host is down` - The bluetooth device is connected to the device.
2. `Connection timed out` - The bluetooth device is powered off.
3. `Connection reset by peer` - The device bluetooth is turned off.

# In case...
If the tool is not working, then type the following command to restart bluetooth services :
```
sudo service bluetooth restart
```
