import os
import logging
from dotenv import load_dotenv

# I-load ang mga variables mula sa .env file
load_dotenv()

# I-define ang Custom Error sa itaas para iwas sa scoping/definition errors
class ConnectionTimeoutError(Exception): 
    pass

# 1. I-configure ang Logging Engine ng Python
# Gagawa ito ng file na 'network_errors.log' at doon isusulat ang mga mangyayari
logging.basicConfig(
    filename="network_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

SIMULATION_MODE = False

device_user = os.getenv("DEVICE_USER")
device_pass = os.getenv("DEVICE_PASS")

print("=========================================")
print("     MODULE 4: LOGGING ERRORS TO FILE    ")
print("=========================================")

network_devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": device_user,
        "password": device_pass,
        "name": "Core-Switch-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.99", # ⚠️ DOWN / OFFLINE DEVICE
        "username": device_user,
        "password": device_pass,
        "name": "Access-Switch-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.3",
        "username": device_user,
        "password": device_pass,
        "name": "Access-Switch-02"
    }
]

for device in network_devices:
    print(f"\n[LOOP] Sinusubukang i-configure ang: {device['name']} ({device['host']})...")
    
    try:
        if SIMULATION_MODE:
            print(f"   [SIMULATION] Connected to {device['name']}.")
        else:
            print(f"   -> Kumokonekta sa {device['host']}...")
            
            # I-trigger ang timeout error para sa offline switch
            if device["host"] == "192.168.1.99":
                raise ConnectionTimeoutError(f"Netmiko Timeout: Hindi maabot ang {device['host']} pagkatapos ng 15 segundo.")
            else:
                print(f"   ✅ [MOCK LIVE] Matagumpay na naipadala ang config sa {device['name']}!")

    except Exception as error_message:
        print(f"   ❌ [ERROR] Hindi ma-konekta ang {device['name']}. Tingnan ang log file!")
        
        # 2. ISULAT ANG ERROR SA LOG FILE: Imbes na sa terminal lang, permanenteng ire-record ito
        logging.error(f"Failed to configure {device['name']} ({device['host']}). Error: {error_message}")

print("\n=========================================")
print(" PROSESO TAPOS: Suriin ang iyong folder para sa log file! ")
print("=========================================")