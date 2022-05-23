from sys import stderr, stdin, stdout
import paramiko
import os

from config import LOGS_PATH, ROOT_DIR


# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # ssh.connect(hostname=HOST, username=USER, key_filename='cdn', port=21)
# ssh.connect(hostname='127.0.0.1', username='admin', password='admin', banner_timeout=200, port=21)
# # print(dir(ssh))
# # stdin, stdout, stderr = ssh.exec_command('ls -lrt /etc#')
# ftp_client = ssh.open_sftp()
# # ftp_client.chdir('/home/vsftpd')
# # print(ftp_client.getcwd())
# # print(os.path.join(os.getcwd(), 'cdn'))
# # ftp_client.put(ROOT_DIR, '/home/vsftpd/cdn')
# print(dir(ftp_client))
# # ftp_client.get(IMG_COMPRESS_PATH)
# # ftp_client.close()
# ssh.close()
# # print(stdout.readlines())

paramiko.util.log_to_file(f"{LOGS_PATH}paramiko.log")
# Open a transport
host,port = "test.rebex.net",22
transport = paramiko.Transport((host,port))

# Auth    
username,password = "demo","password"
transport.connect(None,username,password )

# Go!    
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
filepath = "/pub/example/KeyGenerator.png"
localpath = "/pub/example/"
sftp.get(filepath,localpath)

# Upload
filepath = ROOT_DIR
localpath = "/home/medelkouch/workspace/image-optimizer/"
sftp.put(localpath,filepath)

if sftp: sftp.close()
if transport: transport.close()
