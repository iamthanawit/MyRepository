# ########## Sending commands to FortiGate ##########
# from NetworkAutomation.Paramiko import myParamiko
#
# #myclient = myParamiko.getConnect('fg02.bkk2.vpls.local', '19500', 'vplsadmin', 'K2ag-Sf2@!')
# myclient = myParamiko.getConnect('172.16.215.109', '22', 'admin', 'admin')
# myshell = myParamiko.invokeShell(myclient)
#
# mycmd = 'get system status'
#
# mylist = []
# for x in mycmd.split(';'):
#     mylist.append(x)
# print(mylist)
#
# for y in mylist:
#     myParamiko.setCommand(myshell, y)
#     myoutput = myParamiko.getResult(myshell)
#     print(myoutput)
#
#

######### Get version and hostname ##########
from NetworkAutomation.Paramiko import myParamiko
import ast
myclient = myParamiko.getConnect('172.16.215.109', '22', 'admin', 'admin')
myshell = myParamiko.invokeShell(myclient)

cmd1 = 'get system status'

myParamiko.setCommand(myshell, cmd1)
myoutput = myParamiko.getResult(myshell)

myoutput_list = myoutput.splitlines()[3:-2]
myoutput_text = '\n'.join([str(i) for i in myoutput_list])
print(myoutput_text)







# mydict = dict((x.strip(), y.strip())
#             for x, y in (element.split(': ')
#                          for element in myoutput_text.split('\n')))

# myfirewallname = myoutput_list[18:-13]
# myversion = myoutput_list[3:4]

# firewallname = ''.join(myfirewallname).split(': ')
# version = ''.join(myversion).split(': ')
#
# myversion = version[1]
# myfirewallname = firewallname[1]
#
# print(f'{myfirewallname},{myversion}')

# mylastoutput = '\n'.join(myoutput_list)
# print(mylastoutput)
