import os
import logging
from config.devices import network_devices

class ConnectionTimeoutError(Exception): 
    pass

logging.basicConfig(
    filename="network_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

SIMULATION_MODE = False

# 1. BASAHIN ANG MGA UTOS MULA SA EXTERNAL TEXT FILE
commands_file = "commands.txt"
vlan_configs = []

if os.path.exists(commands_file):
    with open(commands_file, "r") as file:
        # Hahatiin ang bawat linya at tatanggalin ang mga extrang spaces/newlines
        vlan_configs = [line.strip() for line in file if line.strip()]
else:
    print(f"⚠️ Babala: Hindi nahanap ang {commands_file}. Gagamit ng default backup commands.")
    vlan_configs = ["vlan 99", "name Default_Fallback", "exit"]

print("=========================================")
print("    MODULE 6: EXTERNAL COMMAND INPUT     ")
print("=========================================")
print(f"📄 Matagumpay na nabasa ang mga commands mula sa {commands_file}:")
for cmd in vlan_configs:
    print(f"   -> [READY] {cmd}")

# 2. PATAKBUHIN ANG LOOP SA MGA DEVICES
for device in network_devices:
    print(f"\n[LOOP] Sinasimulan ang: {device['name']} ({device['host']})...")
    
    try:
        if SIMULATION_MODE:
            print(f"   [SIMULATION] Connected to {device['name']}.")
        else:
            print(f"   -> Kumokonekta sa {device['host']}...")
            
            if device["host"] == "192.168.1.99":
                raise ConnectionTimeoutError(f"Netmiko Timeout: Hindi maabot ang {device['host']}.")
            else:
                print(f"   ✅ [MOCK LIVE] Naipadala ang mga sumusunod sa {device['name']}:")
                for cmd in vlan_configs:
                    print(f"      Applied: {cmd}")

    except Exception as error_message:
        print(f"   ❌ [ERROR] May problema sa {device['name']}. Logged!")
        logging.error(f"Failed to configure {device['name']} ({device['host']}). Error: {error_message}")

print("\n=========================================")
print("  LESSON 1 PASSED: External data linked! ")
print("=========================================")