import logging
# ETO ANG MAGIC: Ina-import natin ang network_devices mula sa config folder!
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
vlan_configs = ["vlan 30", "name Guest_VLAN", "exit"]

print("=========================================")
print("   MODULE 5: MODULAR ARCHITECTURE TEST   ")
print("=========================================")
print(f"📦 Matagumpay na nai-load ang {len(network_devices)} devices mula sa config/devices.py!")

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
                print(f"   ✅ [MOCK LIVE] Matagumpay na naipadala ang config sa {device['name']}!")

    except Exception as error_message:
        print(f"   ❌ [ERROR] May problema sa {device['name']}. Logged!")
        logging.error(f"Failed to configure {device['name']} ({device['host']}). Error: {error_message}")

print("\n=========================================")
print(" ARCHITECTURE TEST PASSED: Super clean code! ")
print("=========================================")