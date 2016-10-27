import paramiko 
import sys 



def get_ssh_client(self):

 host = sys.argv[1]

 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 ssh.connect(host,username="packetscaper",password="packetscaper")

 return ssh

