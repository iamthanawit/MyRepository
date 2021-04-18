from NetworkAutomation.Paramiko import myParamiko

router1 = {'hostname_input': '172.16.215.211', 'port_input': '22', 'username_input': 'root', 'password_input': 'cisco'}
#router2 = {'hostname_input': '172.16.215.212', 'port_input': '22', 'username_input': 'root', 'password_input': 'cisco'}
#router3 = {'hostname_input': '172.16.215.213', 'port_input': '22', 'username_input': 'root', 'password_input': 'cisco'}

#routers = [router1, router2, router3]
routers = [router1]

now = myParamiko.datetime.utcnow()
year = now.year
month = now.month
day = now.day
hour = '%02d' % now.hour
minute = '%02d' % now.minute

for router in routers:
    myclient = myParamiko.getConnect(**router)
    myshell = myParamiko.invokeShell(myclient)

    myParamiko.setCommand(myshell, 'term len 0')
    myParamiko.setCommand(myshell, 'enable')
    myParamiko.setCommand(myshell, 'cisco')
    myParamiko.setCommand(myshell, 'show run')

    myoutput = myParamiko.getResult(myshell)
    print(myoutput)

    myoutput_list = myoutput.splitlines()
    myoutput_list = myoutput_list[10:-2]
    print(myoutput_list)

    mylastoutput = '\n'.join(myoutput_list)
    print(mylastoutput)

    file_name = f'{router["hostname_input"]}_{year}-{month}-{day}_{hour}-{minute}_UTC.txt'

    with open(file_name, 'w') as file:
        file.write(mylastoutput)