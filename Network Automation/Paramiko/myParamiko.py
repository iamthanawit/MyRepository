import paramiko
import time
from datetime import datetime

def getConnect(hostname_input, port_input, username_input, password_input):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {hostname_input}')
    ssh_client.connect(hostname=hostname_input, port=port_input, username=username_input, password=password_input, look_for_keys=False, allow_agent=False)
    return ssh_client

def invokeShell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def setCommand(shell, command, timeout=1):
    print(f'Sending commands: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def getResult(shell, n=10000):
    myoutput = shell.recv(n).decode()
    return myoutput

def getClose(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print(f'Closing connection')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'hostname_input': '172.16.215.211', 'port_input': '22', 'username_input': 'root', 'password_input': 'cisco'}

    myclient = getConnect(**router1)
    myshell = invokeShell(myclient)

    setCommand(myshell, 'enable')
    setCommand(myshell, 'cisco')
    setCommand(myshell, 'term len 0')
    setCommand(myshell, 'sh ver')
    setCommand(myshell, 'sh ip int br')

    myoutput = getResult(myshell)
    print(myoutput)
