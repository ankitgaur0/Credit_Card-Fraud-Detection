#file is used for creating training pipeline

import os,sys
from pathlib import Path
import pandas as pd
from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.component.Data_Ingestion import Data_Ingestion
from src.component.Data_Transformation import Data_Transformation


try:
    logging.info("training pipeline is starting")
    #make the object of the Data_Ingestion module
    Data_Ingestion_obj=Data_Ingestion()
    (train_data_path,test_data_path)=Data_Ingestion_obj.data_initiate()

    #make the obj of the Data_Transformation module
    Data_Transformation_obj=Data_Transformation()
    train_array,test_array=Data_Transformation_obj.initiate_data_transformation(train_data_path,test_data_path)





except Exception as e:
    raise Custom_Exception(e,sys)

