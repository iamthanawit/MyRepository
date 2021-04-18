import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


mylinux = {'hostname': '172.16.215.91', 'port': '22', 'username': 'root', 'password': 'P@55w0rd'}

### Open SSH Connection ###
print(f'Connection to {mylinux["hostname"]}')
ssh_client.connect(**mylinux, look_for_keys=False, allow_agent=False)

################ Sending commands to targeted devices ################
shell = ssh_client.invoke_shell()
shell.send(b'cat /etc/passwd\n')
time.sleep(1)

# shell.send(b'su -\n')
# time.sleep(1)
# shell.send(b'P@55w0rd\n')
# shell.send(b'cat /etc/shadow\n')
# time.sleep(1)

myoutput = shell.recv(1000000).decode('utf-8')
print(myoutput)
################ Sending commands to targeted devices ################

### Close SSH Connection ###
if ssh_client.get_transport().is_active() == True: ## If the session is still active, then closing the connection!
    print('Closing connection')
    ssh_client.close()