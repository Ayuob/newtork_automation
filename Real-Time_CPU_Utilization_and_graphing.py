import os
import subprocess
import time
import matplotlib.pyplot as plt

def check_reachability(ip_address)
    # Same as in Task 1

def read_devices_file(file_path)
    # Same as in Task 1

def read_login_file(file_path)
    # Same as in Task 1

def read_commands_file(file_path)
    # Same as in Task 1

def apply_commands(device_name, ip_address, username, password, commands)
    print(fApplying commands on device {device_name} ({ip_address}))
    
    # Connect to the device and apply the commands
    # Same as in Task 1
    
    # Retrieve the CPU utilization
    cpu_utilization_cmd = 'get_cpu_utilization_command'  # Replace with the actual command to retrieve CPU utilization
    cpu_utilization_result = subprocess.run([cpu_utilization_cmd], capture_output=True, text=True)
    
    # Save the CPU utilization result to a file
    with open('cpu_utilization.txt', 'a') as file
        file.write(f{time.time()},{ip_address},{cpu_utilization_result.stdout.strip()}n)

def plot_cpu_utilization()
    timestamps = []
    cpu_values = []
    with open('cpu_utilization.txt', 'r') as file
        for line in file
            timestamp, ip_address, cpu_value = line.strip().split(',')
            timestamps.append(float(timestamp))
            cpu_values.append(float(cpu_value))

    plt.plot(timestamps, cpu_values)
    plt.xlabel('Timestamp')
    plt.ylabel('CPU Utilization (%)')
    plt.title('Router CPU Utilization')
    plt.show()

def main()
    # Same as in Task 1
    
    # Apply commands on each device and save CPU utilization in real-time
    for ip_address, device_name in devices.items()
        if ip_address in login_info and ip_address in commands
            username, password = login_info[ip_address]
            while True
                apply_commands(device_name, ip_address, username, password, commands[ip_address])
                time.sleep(5)  # Wait for 5 seconds between each iteration
        else
            print(fLogin information or commands not found for device {device_name} ({ip_address}).)

if __name__ == '__main__'
    main()
