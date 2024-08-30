#this file is used to ingest the data
import os,sys
from pathlib import Path
import pandas as pd
import numpy as np
from src.Logger import logging
from src.Exception_handler import Custom_Exception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngest_config:
    raw_data_path :str = os.path.join("artifacts","raw_data.csv")
    train_data_path :str = os.path.join("artifacts","train_data.csv")
    test_data_path :str = os.path.join("artifacts","test_data.csv")


class Data_Ingestion:
    def __init__(self):
        self.config_obj=DataIngest_config()
    def data_initiate(self):
        try:
            logging.info("Data Ingestion is starting to load data ")

            data=pd.read_csv(Path(os.path.join("D:/credit_card_fraud/notebook/Data","creditcard.csv")))
            logging.info("data is stored in the data variable by pandas function")

            #now making the directory of artifacts to store the data
            os.makedirs(os.path.join(os.path.dirname(self.config_obj.raw_data_path)),exist_ok=True)
            #now store the raw data to raw_data.csv file
            data.to_csv(self.config_obj.raw_data_path)

            #now split the data
            train_data,test_data=train_test_split(data,test_size=0.30,random_state=30,stratify=data["Class"])
            logging.info("spliting the data in the train and test is completed")

            os.makedirs(os.path.join(os.path.dirname(self.config_obj.train_data_path)),exist_ok=True)
            #storing the train data inthe train_data.csv artifacts file
            train_data.to_csv(self.config_obj.train_data_path)
            logging.info("train_data is stored completed in artifacts folder  ")
            os.makedirs(os.path.join(os.path.dirname(self.config_obj.test_data_path)),exist_ok=True)
            #storing the test data in the test_data.csv artifacts file
            test_data.to_csv(self.config_obj.test_data_path)
            logging.info("test_data is stored completed in artifacts folder  ")

            logging.info("return the train and test artifacts path")

            return(
                self.config_obj.train_data_path,
                self.config_obj.test_data_path
            )
        except Exception as e:
            raise Custom_Exception(e,sys)



