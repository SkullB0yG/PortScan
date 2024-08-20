# PortScan
 This Python script scans TCP ports on a specified IP using socket and colorama for terminal color. It offers two modes: easy (scans common ports) and hard (scans all ports). Open ports are displayed in green, and error messages in red. Ideal for quick network audits.
 
 
## Main Functionality

#### Easy Mode:

*Scans a predefined set of common TCP ports, such as port 80 for HTTP and port 22 for SSH.
Ideal for a quick check of the most common ports on a system.*

#### Hard Mode:
*Performs a comprehensive scan of all TCP ports, from port 0 to 65535.
Allows for a more thorough exploration of the target IP address but may take more time.
Colors Used*

- Green: Indicates that the port is open.
- Red: Indicates that no open ports were found.
- Magenta: Used for header messages.
- Cyan: Used for mode descriptions.
- White: Used for user input prompts.


## Requirements

- Python 3.x
- `colorama` library



## Windows Install
```cmd
pip install colorama
git clone https://github.com/SkullB0yG/PortScan.git
```
Enter the directory where you downloaded the project and you can run it with the following command

```cmd
python script.py
```

## Linux Install Debian
```bash
pip install colorama 
git clone https://github.com/SkullB0yG/PortScan.git

```
Enter the directory where you downloaded the project and you can run it with the following command

```bash
python3 script.py
```
#### Optional

```bash 
chmod +x script.py
./script.py
```

## Linux Install Arch
```bash
sudo pacman -S python-colorama 
git clone https://github.com/SkullB0yG/PortScan.git

```
Enter the directory where you downloaded the project and you can run it with the following command

```bash
python3 script.py
```
#### Optional

```bash 
chmod +x script.py
./script.py
```


### Example

```less
Select the scan mode
[MODE       DESCRIPTION]
easy    Common port scanning
hard    Scanning all ports

[MODE]@> easy
[DESTINATION IP]@> 192.168.1.1
Port 22 Open [TCP]
Port 80 Open [TCP]
Port 443 Open [TCP]
```


