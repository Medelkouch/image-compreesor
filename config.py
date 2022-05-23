DEBUG = True


# database config
DB_CONFIG = {
    'host': '9000',
    'database': 'db',
    'user': 'root',
    'password': 'root',
}

# images folder absolutes path end with '/'
ROOT_DIR='/home/medelkouch/workspace/image-optimizer/cdn/'
IMG_COMPRESS_PATH = ROOT_DIR + 'tiny-images/'
RESIZED_PATH = ROOT_DIR + 'tiny-images-plus-2/'
LOGS_PATH = './logs/'

#configuration sftp

HOST = '127.0.0.1'
USER= 'admin'
PASSWORD= 'admin'


# preprocessing config
IMG_WIDTH = 200  # unused !
IMG_HEIGHT = 150  # unused !
IMG_QUALITY = 40
