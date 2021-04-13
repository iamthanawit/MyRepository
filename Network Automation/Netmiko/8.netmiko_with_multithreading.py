from datetime import datetime
from netmiko import ConnectHandler
import time
import threading

start = time.time()

def backup(input_from_outside):
       now = datetime.utcnow()
       year = now.year
       month = now.month
       day = now.day
       hour = now.hour
       minute = now.minute
       sec = now.second

       print(f'########## Connecting to {input_from_outside["host"]} ##########')
       myconnection = ConnectHandler(**input_from_outside)

       print('Entering the enable mode...')
       myconnection.enable() # access to enable mode

       ###########################################################################

       myoutput = myconnection.send_command('show run')

       mypromt = myconnection.find_prompt()
       myhostname = mypromt[0:-1]

       myfilename = f'{myhostname}_BACKUP-{year}-{month}-{day}_{hour}-{minute}-{sec}_UTC.txt'
       with open(myfilename, 'w') as backupfile:
              backupfile.write(myoutput)
              print(f'Backup of {myhostname} completed successfully')
       ###########################################################################

       myconnection.disconnect()
       print(f'########## Disconnecting {input_from_outside["host"]} ##########')




with open('devices.txt', 'r') as f:
       mydevices = f.read().splitlines()
print(f'My devices in list are: {mydevices})')

mythread = []

for ip in mydevices:
       pattern_access_for_device = {
              'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
              'host': ip,
              'username': 'root',
              'password': 'cisco',
              'port': 22,             # optional, default 22
              'secret': 'cisco',      # this is the enable password
              'verbose': True         # optional, default False
              }
       th = threading.Thread(target=backup, args=(pattern_access_for_device, )) #Put the comma to tell python that it is a tuple type.
       mythread.append(th)

print(f'These are your threads: {mythread}')

for th in mythread:
       th.start()

for th in mythread:
       th.join()

end = time.time()
print(f'Total execution time:{end-start}')