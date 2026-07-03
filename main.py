import sys

# Pekein muna natin ang output para sa lab na ito kung offline ang server
SIMULATION_MODE = True

cisco_router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",  # Halimbawang Local Core Switch IP
    "username": "melchor_admin",
    "password": "SecurePassword123",
    "port": 22,
}

print("=========================================")
print("  LESSON 2 & 3: DEVICE CONNECTION LOGIC  ")
print("=========================================")
print(f"Iniaayos ang koneksyon sa: {cisco_router['host']}")

if SIMULATION_MODE:
    print("\n[SIMULATION] Kumokonekta via SSH... (Connecting via Netmiko ConnectHandler)")
    print("✅ [SIMULATION] Matagumpay ang koneksyon!")
    print(f"Nagsasagawa ng command: 'show version | i Version'")
    
    # Ito ang eksaktong hitsura ng ibinabalik na text ng isang totoong Cisco IOS Switch/Router
    mock_output = (
        "Cisco IOS XE Software, Version 17.03.04\n"
        "Cisco IOS Software [Amsterdam], Version 17.3.4, RELEASE SOFTWARE (fc3)"
    )
    
    print("\n--- OUTPUT MULA SA CISCO DEVICE ---")
    print(mock_output)
    print("-----------------------------------\n")
    print("[SIMULATION] Koneksyon ay ligtas na isinara (disconnect).")
else:
    try:
        from netmiko import ConnectHandler
        print("Kumokonekta sa totoong network... (Maaaring tumagal ng ilang segundo)")
        net_connect = ConnectHandler(**cisco_router)
        
        print("✅ Matagumpay ang koneksyon!")
        output = net_connect.send_command("show version | i Version")
        
        print("\n--- OUTPUT MULA SA CISCO DEVICE ---")
        print(output)
        print("-----------------------------------\n")
        
        net_connect.disconnect()
    except Exception as e:
        print(f"❌ Hindi nakakonekta. Error: {e}")

print("=========================================")