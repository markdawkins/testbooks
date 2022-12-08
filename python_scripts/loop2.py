# Import the list of devices from the external file
with open("device_list.txt") as f:
    devices = f.readlines()

# Loop through the list of devices
for device in devices: 
    # Print the device name and MAC address
      print("Device:", device[0:7])
      print("Mac address:", device[8:25])
     
      print (" Test phrase to add in device name here " + device[0:7])
      print (" Test phrase to add in mac address here " + device[8:25])
