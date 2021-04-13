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
myprompt = myconnection.find_prompt() # getting the router's prompt

print(f'########## Connecting to {cisco_device["host"]} ##########')

###########################################################################

if '>' in myprompt:
       myenable = myconnection.enable() # entering the enable mode
       print(myprompt)
       print(myenable)
       myoutput = myconnection.send_command('sh run')
       print(myoutput)

if myconnection.check_config_mode() == False: # returns True if it's already in the global config mode
       myglobalconfig = myconnection.config_mode()  # entering the global config mode
       print(myglobalconfig)
       myconnection.send_command('username u3 secret cisco')

#print(myconnection.check_config_mode())
if myconnection.exit_config_mode() == True: # returns True if it's already in the global config mode
       myconnection.exit_config_mode()  # exiting the global config mode
       print(myconnection.check_config_mode())

###########################################################################

print('########## Disconnecting ##########')
myconnection.disconnect()