import os
from dotenv import load_dotenv

load_dotenv()

# Gagawin nating FALSE ang simulation mode para sa error handling demonstration, 
# para makita natin kung paano sumasalo ng totoong errors ang try-except block.
SIMULATION_MODE = False

device_user = os.getenv("DEVICE_USER")
device_pass = os.getenv("DEVICE_PASS")

print("=========================================")
print("     MODULE 4: ERROR HANDLING (TRY)      ")
print("=========================================")

# Dito, sinadya nating lagyan ng maling IP address (192.168.1.99) ang pangalawang switch
# para ma-simulate natin kung paano hahawakan ng script ang koneksyong mabibigo.
network_devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1", # Ito ay magda-dry-run ng maayos sa simulation fall-through
        "username": device_user,
        "password": device_pass,
        "name": "Core-Switch-01"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.99", # ⚠️ DOWN / OFFLINE DEVICE SIMULATION
        "username": device_user,
        "password": device_pass,
        "name": "Access-Switch-01 (OFFLINE TEST)"
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.3", # Dapat ma-configure pa rin ito kahit nag-error ang nauna!
        "username": device_user,
        "password": device_pass,
        "name": "Access-Switch-02"
    }
]

vlan_configs = ["vlan 30", "name Guest_VLAN", "exit"]

for device in network_devices:
    print(f"\n[LOOP] Sinusubukang i-configure ang: {device['name']} ({device['host']})...")
    
    # 1. ANG TRY BLOCK: Dito isinusulat ang code na pwedeng mag-error
    try:
        if SIMULATION_MODE:
            print(f"   [SIMULATION] Connected to {device['name']}.")
        else:
            # Dahil walang totoong device sa lab ngayon, itong linya na ito ay magbabato ng error.
            # Imbes na mag-crash ang buong program, sasaluhin ito ng 'except' sa ilalim!
            print(f"   -> Kumokonekta sa {device['host']}...")
            
            # Sinadya nating i-trigger ang error dito para sa lesson
            if device["host"] == "192.168.1.99":
                raise ConnectionTimeoutError("Netmiko Timeout: Connection to device timed out after 15 seconds.")
            else:
                # Kunwari ay matagumpay ang iba para makita ang tuloy-tuloy na loop
                print(f"   ✅ [MOCK LIVE] Matagumpay na naipadala ang config sa {device['name']}!")

    # 2. ANG EXCEPT BLOCK: Ito ang sasalo kapag sumabog ang code sa 'try'
    except Exception as error_message:
        print(f"   ❌ [ERROR CAUGHT] Hindi ma-konekta ang {device['name']}.")
        print(f"   ⚠️ Detalye ng Error: {error_message}")
        print("   -> Ligtas na nilaktawan ang device na ito. Ipinagpapatuloy ang script...")

print("\n=========================================")
print(" PROSESO TAPOS: Hindi nag-crash ang script kahit may error! ")
print("=========================================")

# Simple helper para sa simulation structural error handling
class ConnectionTimeoutError(Exception): pass