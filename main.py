import os
from dotenv import load_dotenv

# I-load ang mga variables mula sa .env file
load_dotenv()

SIMULATION_MODE = True

# Hugutin ang iisang secure password/user na ibinabahagi ng mga devices mo (Common Lab Credentials)
device_user = os.getenv("DEVICE_USER")
device_pass = os.getenv("DEVICE_PASS")

print("=========================================")
print("   MODULE 3: MULTI-DEVICE AUTOMATION     ")
print("=========================================")

# 1. Listahan ng maraming devices sa network (Multi-Device Inventory)
network_devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": device_user,
        "password": device_pass,
        "port": 22,
        "name": "Core-Switch-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.2",
        "username": device_user,
        "password": device_pass,
        "port": 22,
        "name": "Access-Switch-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.3",
        "username": device_user,
        "password": device_pass,
        "port": 22,
        "name": "Access-Switch-02"
    }
]

# Listahan ng VLAN configuration na ibabato sa LAHAT ng switches
vlan_configs = [
    "vlan 20",
    "name IP_Phones_VLAN",
    "exit"
]

# 2. Ang Python For-Loop para sa pag-iterate sa bawat device
for device in network_devices:
    print(f"\n[LOOP] Sinasimulan ang proseso para sa: {device['name']} ({device['host']})...")
    
    if SIMULATION_MODE:
        print(f"   -> Connecting via SSH to {device['host']} using user '{device['username']}'...")
        print("   ✅ Matagumpay ang koneksyon!")
        print("   -> Ipinapadala ang mga configuration commands...")
        
        for cmd in vlan_configs:
            print(f"      Applying: {cmd}")
            
        print(f"   ✅ [SIMULATION] Tapos na i-configure ang {device['name']}. Ligtas na dinisconnect.")
        print("-" * 50)
        
    else:
        try:
            from netmiko import ConnectHandler
            # Gagawa ng kopya ng dictionary na walang 'name' key para hindi mag-error si Netmiko
            netmiko_device = device.copy()
            netmiko_device.pop("name")
            
            print(f"   -> Kumokonekta nang live sa {device['name']}...")
            net_connect = ConnectHandler(**netmiko_device)
            
            output = net_connect.send_config_set(vlan_configs)
            print(output)
            
            net_connect.disconnect()
            print(f"   ✅ Tapos na ang {device['name']}.")
        except Exception as e:
            print(f"   ❌ Error sa {device['name']}: {e}")

print("\n=========================================")
print("  PROSESO TAPOS: Lahat ng devices ay napa-run na! ")
print("=========================================")