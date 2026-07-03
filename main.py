import os
import logging
from datetime import datetime
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
        vlan_configs = [line.strip() for line in file if line.strip()]
else:
    vlan_configs = ["vlan 99", "name Default_Fallback", "exit"]

print("=========================================")
print("    MODULE 6: ENTERPRISE BACKUP ENGINE   ")
print("=========================================")

# Siguraduhin natin na may lalagyan ng backups na folder
backup_dir = "backups"
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"📁 Lumikha ng bagong direktoryo: /{backup_dir}\n")

# Kumuha ng kasalukuyang date at time para sa file naming
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

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
                # ====== ENTERPRISE FEATURE: DYNAMIC BACKUP CREATION ======
                # Kunwari ay nag-execute tayo ng "show running-config" sa switch
                mock_running_config = f"! Running configuration backup for {device['name']}\n! Saved on: {current_time}\ninterface GigabitEthernet0/1\n switchport mode access\n!"
                
                # I-define ang pangalan ng file: e.g., backups/Core-Switch-01_20260703_120000.cfg
                backup_filename = f"{backup_dir}/{device['name']}_{current_time}.cfg"
                
                with open(backup_filename, "w") as backup_file:
                    backup_file.write(mock_running_config)
                
                print(f"   💾 [BACKUP SAVED] Na-save ang configuration sa: {backup_filename}")
                # ========================================================
                
                print(f"   ✅ [MOCK LIVE] Naipadala ang mga bagong config sa {device['name']}:")
                for cmd in vlan_configs:
                    print(f"      Applied: {cmd}")

    except Exception as error_message:
        print(f"   ❌ [ERROR] May problema sa {device['name']}. Logged!")
        logging.error(f"Failed to configure {device['name']} ({device['host']}). Error: {error_message}")

print("\n=========================================")
print("   MODULE 6 COMPLETE: Enterprise Ready!   ")
print("=========================================")