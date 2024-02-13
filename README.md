# BlueStorm
A tool which perform deauthentication attack on unpaired bluetooth devices.

<h1>Setup</h1>
Make sure the python and pip3 is installed on your system (Windows/Linux/MacOS).<br>
<h1>Tested Systems</h1>
The tool is currently tested on : <br>
1. Kali Linux<br>
2. Raspberry Pi OS<br>
The testing is going on different systems.

<h1>Install and Run</h1>
1. Run the following command to start terminal in root :<br>

```
sudo su -
```

2. Run the following command to check bluetooth interfaces and its status on your system :<br>

```
hciconfig
```

3. Run the following command to start bluetooth interface if it is not started :<br>

```
hciconfig hciX up
```
where, X is a number starts from 1.<br>
Example - hciconfig hci0 up<br>
4. Download or Clone the Repository.<br>
5. Open the folder and run the <i>BlueStorm.py</i> file by type the following command :<br><br>

```
python3 BlueStorm.py
```
# Includes
Use a bluetooth adapter.

<h1>Key Features</h1>
<b>1. Simple and Clean Menu.</b><br>
<b>2. Show scanned bluetooth devices in a table.</b><br>
