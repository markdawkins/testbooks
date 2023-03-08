#!/usr/bin/env python
from netmiko import ConnectHandler
import time
from getpass import getpass

LIST = input("Enter List Name:")
password = getpass("Enter password: ")
REPORT = input("Enter Report Name:")
reportname = "./REPORTS/VLAN_REPORTS/%s.csv" % REPORT
listname = "./LISTS/%s.txt"  % LIST

print ("Writing output to REPORTS directory...")
time.sleep(1)

file = open(reportname , 'w')

f = open (listname)

for line in f:
    host = line.strip()
    iosv_l2 = {
             'device_type':'cisco_ios',
             'ip':host,
             'username':'admin',
             'password':password,
           }

    net_connect = ConnectHandler(**iosv_l2)
    print(host)

    output0 = net_connect.send_command('show run | inc hostname')
    print(output0[9:25])
    file.write(output0[9:25])

    output1 = net_connect.send_command('show vlan ID 20-25')
    print(output1)
    file.write(host)
    file.write (output1)
    net_connect.send_command('end\n')
    time.sleep(1)
