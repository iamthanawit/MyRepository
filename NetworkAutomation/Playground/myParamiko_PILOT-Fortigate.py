########## Sending commands to FortiGate ##########
from NetworkAutomation.Paramiko import myParamiko

#myclient = myParamiko.getConnect('fg02.bkk2.vpls.local', '19500', 'vplsadmin', 'K2ag-Sf2@!')
myclient = myParamiko.getConnect('172.16.215.109', '22', 'admin', 'admin')
myshell = myParamiko.invokeShell(myclient)

mycmd = 'get system status'

mylist = []
for x in mycmd.split(';'):
    mylist.append(x)
print(mylist)

for y in mylist:
    myParamiko.setCommand(myshell, y)
    myoutput = myParamiko.getResult(myshell)
    print(myoutput)



########## Get version and hostname ##########
# from NetworkAutomation.Paramiko import myParamiko
#
# myclient = myParamiko.getConnect('172.16.215.109', '22', 'admin', 'admin')
# myshell = myParamiko.invokeShell(myclient)
#
# mycmd = 'get system status'
#
# myParamiko.setCommand(myshell, mycmd)
# myoutput = myParamiko.getResult(myshell)
#
# myoutput_list = myoutput.splitlines()
# myfirewallname = myoutput_list[18:-13]
# myversion = myoutput_list[3:4]
#
# myfirewallname = ''.join(myfirewallname)
# myversion = ''.join(myversion)
#
# print(f'{myfirewallname}\n{myversion}')
#
# # mylastoutput = '\n'.join(myoutput_list)
# # print(mylastoutput)