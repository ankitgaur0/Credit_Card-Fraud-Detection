import os,sys
from pathlib import Path
import logging
from datetime import datetime


log_file_name=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
#file path where Logs folder will be created
logs_path=os.path.join(os.getcwd(),"Logs",log_file_name)
os.makedirs(logs_path,exist_ok=True) 


log_file_path=os.path.join(logs_path,log_file_name)

log_format="[%(asctime)s] %(levelname)s -%(name)s -%(filename)s:%(lineno)d -%(message)s"

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format=log_format
)
