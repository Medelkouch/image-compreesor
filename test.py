import os.path, os
from ftplib import FTP, error_perm

from config import HOST, PASSWORD, PORT, USER


ftp = FTP()
ftp.connect( HOST, PORT)
ftp.login( USER, PASSWORD)
filename_cdn = "cdn"
filename_client = "client"

def placeFiles(path, ftp):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("RETR", name, localpath)
            ftp.retrbinary('RETR ' + name, open(localpath,'wb').write)
        elif os.path.isdir(localpath):
            print("MKD", name)

            try:
                ftp.mkd(name)

            # ignore "directory already exists"
            except error_perm as e:
                if not e.args[0].startswith('550'): 
                    raise

            print("CWD", name)
            ftp.cwd(name)
            placeFiles(localpath, ftp)           
            print("CWD", "..")
            ftp.cwd("..")

placeFiles(filename_cdn, ftp)
placeFiles(filename_client, ftp)

ftp.quit()