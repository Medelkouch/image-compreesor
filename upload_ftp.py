import os.path, os
from ftplib import FTP, error_perm

from img_processing import create_directory

# from config import HOST, PASSWORD, PORT, USER


# ftp = FTP()
# ftp.connect( '192.168.11.105', 20001)
# ftp.login( 'ftpuser', 'user2022')
# filename_cdn = "cdn"
# filename_client = "client"

def placeFiles(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("STOR", name, localpath)
            ftp.storbinary('STOR ' + name, open(localpath,'rb'))
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
            placeFiles(ftp, localpath)           
            print("CWD", "..")
            ftp.cwd("..")
    

# placeFiles(ftp, filename_cdn)
# placeFiles(ftp, filename_client)

# ftp.quit()