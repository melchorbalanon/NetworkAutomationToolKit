import sys

SIMULATION_MODE = True

cisco_router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "melchor_admin",
    "password": "SecurePassword123",
    "port": 22,
}

print("=========================================")
print("     LESSON 4: CONFIGURATION CHANGES     ")
print("=========================================")

# Listahan ng mga commands na gusto nating i-auto-configure sa switch/router
config_commands = [
    "interface GigabitEthernet0/1",
    "description Link to Core_Switch_01 - Configured via Python",
    "vlan 10",
    "name Management_VLAN",
    "exit"
]

if SIMULATION_MODE:
    print(f"[SIMULATION] Kumokonekta sa {cisco_router['host']} via SSH...")
    print("✅ [SIMULATION] Matagumpay ang koneksyon!")
    
    print("\n--- IPINAPADALANG CONFIGURATION SET ---")
    for cmd in config_commands:
        print(f"Applying: {cmd}")
    print("---------------------------------------\n")
    
    # Ito ang eksaktong hitsura ng ibinabalik ng Cisco kapag nag-conf t ka
    mock_config_output = (
        "configure terminal\n"
        "Enter configuration commands, one per line. End with CNTL/Z.\n"
        "router(config)# interface GigabitEthernet0/1\n"
        "router(config-if)# description Link to Core_Switch_01 - Configured via Python\n"
        "router(config-if)# vlan 10\n"
        "router(config-vlan)# name Management_VLAN\n"
        "router(config-vlan)# exit\n"
        "router(config)# end\n"
        "router#"
    )
    
    print("--- OUTPUT MULA SA DEVICE (SUCCESS) ---")
    print(mock_config_output)
    print("---------------------------------------\n")
    print("[SIMULATION] Ligtas na isinara ang koneksyon at nai-save ang changes.")

else:
    try:
        from netmiko import ConnectHandler
        print("Kumokonekta sa totoong network...")
        net_connect = ConnectHandler(**cisco_router)
        
        # Gagamitin ang .send_config_set() para sa listahan ng config commands
        print("Ipinapadala ang mga configuration changes...")
        output = net_connect.send_config_set(config_commands)
        
        print("\n--- OUTPUT MULA SA DEVICE ---")
        print(output)
        print("-----------------------------\n")
        
        net_connect.disconnect()
    except Exception as e:
        print(f"❌ Error encountered: {e}")

print("=========================================")