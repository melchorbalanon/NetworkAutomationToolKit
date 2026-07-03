import os
from dotenv import load_dotenv

# 1. I-load ang mga variables mula sa .env file
load_dotenv()

SIMULATION_MODE = True

# 2. Hugutin ang credentials para sa Device Connection Dictionary
cisco_router = {
    "device_type": "cisco_ios",
    "host": os.getenv("DEVICE_HOST"),
    "username": os.getenv("DEVICE_USER"),
    "password": os.getenv("DEVICE_PASS"),
    "port": 22,
}

print("=========================================")
print("  MODULE 3: SECURE CONFIGURATION CHANGE   ")
print("=========================================")

# Siguraduhin muna na may laman ang hinugot na credentials
if not cisco_router["host"] or not cisco_router["username"]:
    print("❌ Error: Kulang ang detalye sa iyong .env file!")
    exit()

# Listahan ng mga commands na i-o-automate
config_commands = [
    "interface GigabitEthernet0/1",
    "description Link to Core_Switch_01 - Configured via Python Securely",
    "vlan 10",
    "name Management_VLAN",
    "exit"
]

if SIMULATION_MODE:
    print(f"[SIMULATION] Ikokonekta sa secure host: {cisco_router['host']}")
    print(f"[SIMULATION] Gagamitin ang user: {cisco_router['username']}")
    print("✅ [SIMULATION] Matagumpay ang koneksyon via SSH!")
    
    print("\n--- IPINAPADALANG CONFIGURATION SET ---")
    for cmd in config_commands:
        print(f"Applying: {cmd}")
    print("---------------------------------------\n")
    
    mock_config_output = (
        "configure terminal\n"
        "Enter configuration commands, one per line. End with CNTL/Z.\n"
        "router(config)# interface GigabitEthernet0/1\n"
        "router(config-if)# description Link to Core_Switch_01 - Configured via Python Securely\n"
        "router(config-if)# vlan 10\n"
        "router(config-vlan)# name Management_VLAN\n"
        "router(config-vlan)# exit\n"
        "router(config)# end\n"
        "router#"
    )
    
    print("--- OUTPUT MULA SA SECURE DEVICE ---")
    print(mock_config_output)
    print("---------------------------------------\n")
    print("[SIMULATION] Koneksyon ay ligtas na isinara.")

else:
    try:
        from netmiko import ConnectHandler
        print(f"Kumokonekta nang live sa {cisco_router['host']}...")
        net_connect = ConnectHandler(**cisco_router)
        
        print("Ipinapadala ang mga configuration changes...")
        output = net_connect.send_config_set(config_commands)
        
        print("\n--- OUTPUT MULA SA DEVICE ---")
        print(output)
        print("-----------------------------\n")
        
        net_connect.disconnect()
    except Exception as e:
        print(f"❌ Error encountered: {e}")

print("=========================================")