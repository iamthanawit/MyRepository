with open('devices.txt', 'r') as file:
    myfile = file.read().splitlines()

from netmiko import ConnectHandler


for ip in myfile:
    cisco_device = {
           'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
           'host': ip,
           'username': 'root',
           'password': 'cisco',
           'port': 22,             # optional, default 22
           'secret': 'cisco',      # this is the enable password
           'verbose': True         # optional, default False
           }

    myconnection = ConnectHandler(**cisco_device)
    print('##### Connecting #####')
    ###########################################################################
    mylist = []
    myoutput = myconnection.send_command('sh ip int br | ex unas ')
    myoutput_list = mylist.append(myoutput)



    for i in myoutput.split('\n'):
        if 'administratively down' in i:
            interface_down_list = i.split(' ')
            for intdown in interface_down_list[0:1]:
                print(f'We found {intdown} of host IP {ip} is down')
                askforshut = input(f'You would like to no shutdown {intdown}? If yes, type "no sh": ')
                mycommands = ['int ' + intdown, 'no sh', 'end']
                if 'no s' in askforshut:
                    myconnection.enable()
                    if myconnection.check_config_mode() == False:  # returns True if it's already in the global config mode
                        myglobalconfig = myconnection.config_mode()  # entering the global config mode
                        print(myglobalconfig)
                        myoutput = myconnection.send_config_set(mycommands)
                        print(myoutput)
                    print(myconnection.find_prompt())
            else:
                break
        else:
            continue
    print('There is no interfaces down :)')



    ###########################################################################
    print('##### Closing connection #####')
    myconnection.disconnect()