import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


def create_connection(host, user, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        return None
    return connection


def flag_optimized_images(images):
    connection = create_connection(** DB_CONFIG)
    if connection:
        images_ids = tuple([img.id for img in images])
        flag_images = ("INSERT INTO images ",
                       "(id, compressed) ",
                       "VALUES (%s, 1), (%s, 1), (%s, 1), (%s, 1) ",
                       "ON DUPLICATE KEY UPDATE compressed = VALUES(compressed)")
        ##
        try:
            cursor = connection.cursor()
            cursor.execute(flag_images, images_ids)

            # Make sure data is committed to the database
            connection.commit()
        except Exception as e:
            print(f"( exception msg: {e} )")
            return None
        else:
            cursor.close()
            connection.close()
            return True
    else:
        # Log
        print('Error to etablish connexion ')
        return None
