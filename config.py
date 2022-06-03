DEBUG = True


# database config
DB_CONFIG = {
    'host': '80',
    'database': 'db',
    'user': 'root',
    'password': 'root',
}

# images local folder absolutes path end with '/'
ROOT_DIR='./client/'
ROOT_DIR_PATH = './cdn/'
IMG_COMPRESS_PATH = ROOT_DIR_PATH + 'tiny-images/'
RESIZED_PATH = ROOT_DIR_PATH + 'tiny-images-plus-2/'

# # images remote folder absolutes path end with '/'
ROOT_DIR_REMOTE_IMAGES='./ftp_server/images/'
ROOT_DIR_REMOTE= './ftp_server/'
IMG_COMPRESS_REMOTE_PATH = ROOT_DIR_REMOTE + 'compressed/'
RESIZED_REMOTE_PATH = ROOT_DIR_REMOTE + 'resized/'


LOGS_PATH = './logs/'

#configuration sftp

HOST = '127.0.0.1'
USER= 'ftpuser'
PASSWORD= 'user2022'
PORT = 20001


# preprocessing config
IMG_WIDTH = 200  # unused !
IMG_HEIGHT = 150  # unused !
IMG_QUALITY = 50

