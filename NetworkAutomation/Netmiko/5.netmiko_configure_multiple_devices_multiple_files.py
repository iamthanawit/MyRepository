from netmiko import ConnectHandler
with open('devices.txt', 'r') as f:
       mydevices = f.read().splitlines()

mydevices_list = []

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
       mydevices_list.append(cisco_device)

# print(mydevices_list)
# exit(1)

for device in mydevices_list:
       print(f'########## Connecting to {device["host"]} ##########')
       myconnection = ConnectHandler(**device)

       print('Entering the enable mode...')
       myconnection.enable() # access to enable mode
       ###########################################################################

       myfile = input(f'Enter a configuration file (use a valid path) for {device["host"]}: ')

       print(f'Running commands from file: {myfile} on device: {device["host"]}')

       myoutput = myconnection.send_config_from_file(myfile)
       print(myoutput)

       ###########################################################################
       myconnection.disconnect()
       print(f'########## Disconnecting {device["host"]} ##########')

