import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname': '172.16.215.211', 'port': '22', 'username': 'root', 'password': 'cisco'}
router2 = {'hostname': '172.16.215.212', 'port': '22', 'username': 'root', 'password': 'cisco'}
router3 = {'hostname': '172.16.215.213', 'port': '22', 'username': 'root', 'password': 'cisco'}

routers = [router1, router2, router3]

for router in routers:
    ### Open SSH Connection ###

    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    ################ Sending commands to targeted devices ################
    shell.send(b'enable\n')
    shell.send(b'cisco\n')
    shell.send(b'conf t\n')
    shell.send(b'router ospf 1\n')
    shell.send(b'net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send(b'end\n')
    shell.send(b'ter leng 0\n')
    shell.send(b'sh ip protocol\n')
    time.sleep(2)

    output = shell.recv(10000).decode('utf-8')
    print(output)
    ################ Sending commands to targeted devices ################

    ### Close SSH Connection ###
    if ssh_client.get_transport().is_active() == True: # If the session is still active, then closing the connection!
        print('Closing connection')
        ssh_client.close()