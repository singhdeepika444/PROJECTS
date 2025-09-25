import os
import platform
import socket
import psutil
import cpuinfo
from screeninfo import get_monitors
import wmi
import speedtest
import uuid


def get_installed_software():
    software_list = os.popen('wmic product get name').read()
    return software_list

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    return download_speed, upload_speed

def get_screen_resolution():
    try:
        monitors = get_monitors()
        if monitors:
            primary_monitor = monitors[0] # Assuming the first monitor is the primary monitor
            width, height = primary_monitor.width, primary_monitor.height # Extracting width and height of the primary monitor
            
            return width, height
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_system_info():
    system_info = {}
    system_info['OS'] = platform.system() + " " + platform.version()
    c = wmi.WMI()
    for os in c.Win32_OperatingSystem():
        system_info['Windows_Version'] = os.Caption
    
    for processor in c.Win32_Processor():
        system_info['CPU_Model'] = processor.Name
        system_info['CPU_Cores'] = processor.NumberOfCores
        system_info['CPU_Threads'] = processor.NumberOfLogicalProcessors
    
    for gpu in c.Win32_VideoController():
        system_info['GPU_Model'] = gpu.Caption
    system_info['RAM_Size'] = round(psutil.virtual_memory().total / (1024**3), 2)  # in GB
    return system_info

def get_network_info():
    network_info = {}
    network_info['MAC_Address'] = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2, 7)][::-1])
    hostname = socket.gethostname()
    network_info['IP_Address'] = socket.gethostbyname(hostname)
    return network_info

if __name__ == "__main__":
    print("==============================================================================================")
    
    installed_software = get_installed_software()
    print("Installed Software:\n", installed_software)
    
    print("==============================================================================================")
    
    internet_speed = get_internet_speed()
    print("Internet Speed - Download: {} Mbps, Upload: {} Mbps".format(internet_speed[0], internet_speed[1]))
    
    print("==============================================================================================")
    
    screen_resolution = get_screen_resolution()
    if screen_resolution:
        print(f"Screen resolution: {screen_resolution[0]} x {screen_resolution[1]} pixels")
    else:
        print("Unable to retrieve screen resolution.")
        
    print("==============================================================================================")
    
    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
        
    print("==============================================================================================")
    
    network_info = get_network_info()
    print("\nNetwork Information:")
    for key, value in network_info.items():
        print(f"{key}: {value}")
        
    print("==============================================================================================")