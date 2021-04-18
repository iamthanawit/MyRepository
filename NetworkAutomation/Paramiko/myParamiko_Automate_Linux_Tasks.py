import myParamiko

myclient = myParamiko.getConnect('172.16.215.91', '22', 'oat', 'P@55w0rd')
myshell = myParamiko.invokeShell(myclient)

myParamiko.setCommand(myshell, 'uname -a')
myParamiko.setCommand(myshell, 'sudo groupadd developers')
myParamiko.setCommand(myshell, 'P@55w0rd', 2)
myParamiko.setCommand(myshell, 'tail -n 1 /etc/group')

myoutput = myParamiko.getResult(myshell)
print(myoutput)