from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '10.1.1.10',
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

print('Sending commands from file...')
myoutput = myconnection.send_config_from_file('ospf.txt')
print(myoutput)

###########################################################################
myconnection.disconnect()
print('########## Disconnecting ##########')