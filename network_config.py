import os
import subprocess


# def check_reachability(ip_address):
#     # Use subprocess to ping the IP address and check its reachability
#     result = subprocess.run(['ping', '-c', '4', ip_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     return result.returncode == 0
def check_reachability(ip_address):
    command = ['ping', '-n', '4', ip_address]  # Use -n flag for Windows
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return "Reply" in result.stdout

def read_devices_file(file_path):
    devices = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, ip_address = map(str.strip, line.split(','))
            devices[ip_address] = name
    return devices

def read_login_file(file_path):
    login_info = {}
    with open(file_path, 'r') as file:
        for line in file:
            ip_address, username, password = map(str.strip, line.split(','))
            login_info[ip_address] = (username, password)
    return login_info

def read_commands_file(file_path):
    commands = {}
    with open(file_path, 'r') as file:
        for line in file:
            ip_address, *cmds = map(str.strip, line.split(','))
            commands[ip_address] = cmds
    return commands

# def apply_commands(device_name, ip_address, username, password, commands):
#     # Implement the logic to connect to the device and apply the commands
#     # This can be done using the network automation framework of your choice (e.g., Netmiko, Napalm, etc.)
#     print(f"Applying commands on device: {device_name} ({ip_address})")
#     print(f"Commands: {commands}\n")

import paramiko

def apply_commands(device_name, ip_address, username, password, commands):
    try:
        # Connect to the OpenWrt VM using SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip_address, username=username, password=password)

        print(f"Connected to device: {device_name} ({ip_address})")

        # Apply each command to the OpenWrt VM
        for command in commands:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            output = stdout.read().decode('utf-8')
            print(f"Command: {command}")
            print(f"Output:\n{output}\n")

        print(f"Successfully applied commands on device: {device_name} ({ip_address})")

        # Close the SSH connection
        ssh_client.close()

    except Exception as e:
        print(f"Failed to apply commands on device: {device_name} ({ip_address})")
        print(f"Error: {str(e)}\n")


def main():
    devices_file = 'devices.txt'
    login_file = 'login.txt'
    commands_file = 'commands.txt'

    # Check if input files exist
    if not all(os.path.isfile(file) for file in [devices_file, login_file, commands_file]):
        print("One or more input files do not exist.")
        return

    # Read the input files
    devices = read_devices_file(devices_file)
    login_info = read_login_file(login_file)
    commands = read_commands_file(commands_file)

    # Check reachability of each device
    for ip_address in devices.keys():
        if check_reachability(ip_address):
            print(f"Device {devices[ip_address]} ({ip_address}) is reachable.")
        else:
            print(f"Device {devices[ip_address]} ({ip_address}) is not reachable.")

    # Apply commands on each device
    for ip_address, device_name in devices.items():
        if ip_address in login_info and ip_address in commands:
            username, password = login_info[ip_address]
            apply_commands(device_name, ip_address, username, password, commands[ip_address])
        else:
            print(f"Login information or commands not found for device {device_name} ({ip_address}).")

if __name__ == '__main__':
    main()
