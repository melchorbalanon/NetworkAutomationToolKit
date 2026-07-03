import os
from dotenv import load_dotenv

load_dotenv()

device_user = os.getenv("DEVICE_USER")
device_pass = os.getenv("DEVICE_PASS")

# Siguraduhin na walang typo rito sa pangalan:
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
        "host": "192.168.1.99",
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