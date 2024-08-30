import os,sys
from pathlib import Path
import pickle
from src.Logger import logging
from src.Exception_handler import Custom_Exception


def save_obj(dir_path,obj):
    try:
        dir_path=Path(os.path.dirname(dir_path))
        
        os.makedirs(dir_path,exist_ok=True)
        with open(dir_path,"rb") as dir_path:
            pickle.dump(dir_path,obj)
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