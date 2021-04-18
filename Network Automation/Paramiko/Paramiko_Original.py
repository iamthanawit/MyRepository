import paramiko
import time

myssh_client = paramiko.SSHClient()
myssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

### Enter your parameters and start to connect the destination host ###
router = {'hostname': '172.16.215.213', 'port': '22', 'username': 'root', 'password': 'cisco'}

### Open SSH Connection ###
print(f'########## Connecting to {router["hostname"]} ##########')
myssh_client.connect(**router, look_for_keys=False, allow_agent=False)

################ Sending commands to targeted devices ################
shell = myssh_client.invoke_shell() #Invoke every time when you send any single commands.
shell.send(b'terminal length 0\n')
shell.send(b'show version\n')
shell.send(b'sh ip int br\n')

time.sleep(1)
myoutput = shell.recv(10000).decode()
print(myoutput)
################ Sending commands to targeted devices ################

### Close SSH Connection ###
if myssh_client.get_transport().is_active() == True: #Checking is SSH session if it is still active.
    print('########## Closing connection ##########')
    myssh_client.close()