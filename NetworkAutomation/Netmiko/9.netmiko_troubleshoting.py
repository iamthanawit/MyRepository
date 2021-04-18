import time
from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
mylogger = logging.getLogger("netmiko")

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

# myoutput = myconnection.send_command('sh version')
# print(myoutput)

myconnection.write_channel('show version\n')
time.sleep(2)
myoutput = myconnection.read_channel()
print(myoutput)

###########################################################################
print('##### closing connection #####')
myconnection.disconnect()