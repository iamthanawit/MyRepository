import paramiko
import time
### Open SSH Connection ###
myssh_client = paramiko.SSHClient()
myssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

### Enter your parameters and start to connect the destination host ###
router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'root', 'password': 'cisco'}

print(f'########## Connecting to {router["hostname"]} ##########')
myssh_client.connect(**router, look_for_keys=False, allow_agent=False)

### Send your commands ###
myshell = myssh_client.invoke_shell() #Invoke every time when you send any single commands.
myshell.send('terminal length 0\n')
myshell.send('show version\n')
myshell.send('sh ip int br\n')
time.sleep(1)
myoutput = myshell.recv(10000).decode()
print(myoutput)

### Close SSH Connection ###
if myssh_client.get_transport().is_active() == True: #Checking is SSH session if it is still active.
    print('########## Closing connection ##########')
    myssh_client.close()