from datetime import datetime
from netmiko import ConnectHandler
with open('devices.txt', 'r') as f:
       mydevices = f.read().splitlines()
print(f'My devices in list are: {mydevices})')
###########################################################################

now = datetime.utcnow()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
sec = now.second
###########################################################################
for ip in mydevices:

       cisco_device = {
              'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
              'host': ip,
              'username': 'root',
              'password': 'cisco',
              'port': 22,             # optional, default 22
              'secret': 'cisco',      # this is the enable password
              'verbose': True         # optional, default False
              }

       print(f'########## Connecting to {cisco_device["host"]} ##########')
       myconnection = ConnectHandler(**cisco_device)

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
       print(f'########## Disconnecting {cisco_device["host"]} ##########')

