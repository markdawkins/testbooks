from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko import NetMikoAuthenticationException

import time
from getpass import getpass

LIST = input("Enter List Name:")
#password = getpass("Enter password: ")
REPORT = input("Enter Report Name:")
reportname = "\REPORTS\VLAN_REPORTS\%s.csv" % REPORT
listname = "\LISTS\%s.txt"  % LIST

print ("Writing output to REPORTS directory...")
time.sleep(1)

file = open(reportname , 'w')

f = open (listname)

for line in f:
    host = line.strip()
    iosv_l2 = {
             'device_type':'cisco_ios',
             'ip':host,
             'username':'svc_ansible',
             'password':'NhYadAhWE4PQ9X(wz!',
             'timeout': 60
    }

    try:
            net_connect = ConnectHandler(**iosv_l2)
    except (NetMikoAuthenticationException):
           print ('Authentication failure: ' + host )
           continue
    except (NetMikoTimeoutException):
           print ('Timeout to device: ' + host)
           file.write ('Timeout to device: ' + host)
           continue
    except (EOFError):
           print ('End of file while attempting device ' + host)
           file.write ('End of file while attempting device ' + host)
           continue
    except (SSHException):
           print ('SSH Issue. Are you sure SSH is enabled? ' + host)
           file.write ('SSH Issue. Are sure SSH is enabled? ' + host)
           continue
    except Exception as unknown_error:
           print ('some other error: '+ str(unknown_error) )
           file.write('Some other error: ' + str(unknown_error))
           continue

    output0 = net_connect.send_command('show run | inc hostname' , read_timeout=30)
    time.sleep(2)
    print(host)
    print(output0[9:25])
    file.write(output0[9:25])

    output1 = net_connect.send_command('show vlan ID 20-25' , read_timeout=30)
    print(output1)
    file.write (output1)
    time.sleep(1)
