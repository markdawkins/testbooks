from paramiko.client import SSHClient

SSH_USER = "<Insert your ssh user here>"
SSH_PASSWORD = "<Insert your ssh password here>"
SSH_HOST = "<Insert the IP/host of your device/server here>"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()


client.load_system_host_keys()
client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         password=SSH_PASSWORD)


CMD = "show ip interface brief" # You can issue any command you want
stdin, stdout, stderr = client.exec_command(CMD)
client.close()
