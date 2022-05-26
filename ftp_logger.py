from ftplib import FTP

from config import HOST, LOGS_PATH, PASSWORD, PORT, USER

command = "df"

#Update the next three lines with your server's information

FTP.util.log_to_file(f"{LOGS_PATH}logftp.log")

host = HOST
port = PORT
username = USER
password = PASSWORD

ftp = FTP()
ftp.connect( host, port)
ftp.login( username, password)
ftp.retrlines("LIST")