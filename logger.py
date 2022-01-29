import logging
from config import LOGS_PATH

Log_Format = "%(levelname)s | %(asctime)s : %(message)s"
logging.basicConfig(filename=f"{LOGS_PATH}logfile.log",
                    filemode="a",
                    format=Log_Format,
                    level=logging.INFO)

log = logging.getLogger()
