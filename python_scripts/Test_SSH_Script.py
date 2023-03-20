
from paramiko.client import SSHClient, AutoAddPolicy

import getpass
SSH_PASSWORD = getpass.getpass(prompt='Password: ', stream=None)
SSH_USER = input("Username: ")
SSH_HOST = input("Host: ")
SSH_PORT = int(input("Port: "))


SSH_USER = "<Insert your ssh user here>"
SSH_PASSWORD = "<Insert your ssh password here>"
SSH_HOST = "<Insert the IP/host of your device/server here>"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
try:
    client.connect(SSH_HOST, port=SSH_PORT,
                             username=SSH_USER,
                             password=SSH_PASSWORD)
    print("Connected successfully!")
except Exception:
    print("Failed to establish connection.")
