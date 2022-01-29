
from config import IMG_PATH, IMG_COMPRESS_PATH, IMG_QUALITY
from PIL import Image
from hurry.filesize import size
import os
import requests
from logger import log


def create_directory(path):
    folder_exist = os.path.exists(path)
    if not folder_exist:
        os.makedirs(path, exist_ok=False)
        log.info(
            f"New folder added: {path}")


def get_files_directory(folder_id):
    files = os.listdir(IMG_PATH+str(folder_id))
    return files


def get_file_size(file_path):
    size_ = os.path.getsize(file_path)
    return size(size_)


def image_optimizer(image_data, folder_id):
    try:
        fat_img = Image.open(IMG_PATH + folder_id + image_data.name)
        ###
        create_directory(IMG_COMPRESS_PATH + folder_id)
        slim_img_filename = IMG_COMPRESS_PATH + folder_id + image_data.name
        fat_img.save(slim_img_filename, optimize=True,
                     quality=IMG_QUALITY)  # 95 => 50% , 90 => 30%
    except Exception as e:
        log.error(f"Exception msg: {e}")
        return None
    else:
        log.info(
            f"Image ( {fat_img.filename} ) from {get_file_size(fat_img.filename)} to {get_file_size(slim_img_filename)}")
        return True

#######################################################################


def save_img_from_cdn(cdn_, filename):
    response = requests.get(cdn_)
    file = open(IMG_PATH + filename, "wb")
    file.write(response.content)
    file.close()

#save_img_from_cdn("https://i.imgur.com/cG4nUs2.jpeg", "cG4nUs2.jpeg")

#foo = foo.resize((160, 300), Image.ANTIALIAS)
#foo.save("path\\to\\save\\image_scaled.jpg", quality=95)
#foo.save("path\\to\\save\\image_scaled_opt.jpg", optimize=True, quality=95)
