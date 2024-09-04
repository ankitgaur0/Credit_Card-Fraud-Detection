import os,sys
from pathlib import Path
import pickle
from src.Logger import logging
from src.Exception_handler import Custom_Exception


def save_obj(file_path,obj):
    try:
        dir_path=(Path(file_path))
        dir_path=os.path.dirname(dir_path)
        
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file:
            pickle.dump(obj,file)
            logging.info(f"save the obj in the path {dir_path}")
    except Exception as e:
        raise Custom_Exception(e,sys)
    

def load_obj(dir_path):
    try:
        dir_path=Path(dir_path)
        with open(dir_path,"rb") as dir_path_obj:
            logging.info(f"returnt the obj form dir path is {dir_path}")
            return pickle.load(dir_path_obj)
        
    except Exception as e:
        raise Custom_Exception(e,sys)