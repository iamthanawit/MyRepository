from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '10.1.1.10',
       'username': 'admin',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

myconnection = ConnectHandler(**cisco_device)

#########################################################################################################

mytrasfer_output = file_transfer(myconnection, source_file='ospf.txt', dest_file='ospf123.txt', file_system='disk0:', direction='put', overwrite_file=True)
print(mytrasfer_output)

#########################################################################################################

print('##### closing connection #####')
myconnection.disconnect()