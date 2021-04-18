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

#mycommands = ['int loop 0', 'ip addr 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco', 'end', 'wr mem']
#myoutput = myconnection.send_config_set(mycommands)
#mycommands = 'int loop 0;ip addr 1.1.1.1 255.255.255.255;exit;username netmiko secret cisco;end;wr mem'
mycommands = '''int loop 0
ip addr 1.1.1.1 255.255.255.255
exit
username netmiko secret cisco
end
wr mem'''
myoutput = myconnection.send_config_set(mycommands.split('\n')) # access to global configuration mode, and send the commands
print(myoutput)

###########################################################################


myconnection.disconnect()
print('########## Disconnecting ##########')