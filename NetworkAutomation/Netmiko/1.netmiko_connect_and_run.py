# from netmiko import Netmiko
# myconnection = Netmiko(host='10.1.1.10', port='22', username='root', password='cisco', device_type='cisco_ios')

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

myconnection = ConnectHandler(**cisco_device)

###########################################################################

myoutput = myconnection.send_command('sh ip int br')
print(myoutput)

###########################################################################

print('##### closing connection #####')
myconnection.disconnect()