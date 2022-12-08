# Create a list of tuples containing the device name and MAC address
devices = [("Device1", "00:11:22:33:44:55"),
           ("Device2", "66:77:88:99:AA:BB"),
           ("Device3", "CC:DD:EE:FF:00:11")]

# Loop through the list of devices
for device in devices:
    # Get the device name and MAC address
    name, mac_address = device

    # Print the device name and MAC address
    print("Device name:", name)
    print("MAC address:", mac_address)
    
    
    ######THIS IS WHAT THE OUTPUT LOOKS LIKE _#######
    
Device name: Device1
MAC address: 00:11:22:33:44:55
Device name: Device2
MAC address: 66:77:88:99:AA:BB
Device name: Device3
MAC address: CC:DD:EE:FF:00:11
