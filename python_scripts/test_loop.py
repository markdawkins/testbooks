# Imprt the list of devices from the external file 
with open("device_lsit.txt") as f:
    devices = f.readlines()
    
# loop through the list of devices 
for device in devcies:
    # Print the device name an MAC address
    print ("Device:" , device)
