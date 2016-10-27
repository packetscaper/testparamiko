import paramiko 
import sys 


host = sys.argv[1]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,username="packetscaper",password="packetscaper")

print "connected to %s" % host

