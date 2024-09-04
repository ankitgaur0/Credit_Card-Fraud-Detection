import os,sys
import pandas as pd
import numpy as np
from pathlib import Path
from dataclasses import dataclass
import pickle
#some local module

from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.Utils import save_obj

#some extra package of sklearn and imblearn (IamBlance learn SMOTE)
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE


@dataclass
class Datatrans_config:
    preprocessor_path :str = os.path.join("artifacts","preprocessor.pkl")

class Data_Transformation:
    def __init__(self):
        self.Datatrans_config_obj = Datatrans_config()

    def get_data_transformation(self):
        logging.info("get_data_transformation is start")
        try:
            numerical_columns=["Time","Amount"]
            logging.info("making the pipeline for scaling the Amount and Time columns")
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="mean")),
                    ("scaling",StandardScaler())
                ]
            )
            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns)
                ]
            )
            logging.info("return the preprocessor")
            
            return preprocessor
        

        except Exception as e:
            raise Custom_Exception(e,sys)
        
    def initiate_data_transformation(self,train_data_path,test_data_path):
        logging.info("now tranform the data ")
        try:
            logging.info("reading the train and test csv file ")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)

            #remove the duplicate data from the train data
            train_data=train_data[~((train_data["Class"]==0) & train_data.duplicated())]
            #concat the data 
            df=pd.concat([train_data,test_data],axis=0)
            X=df.drop(["Class"],axis=1)
            y=df["Class"]

            logging.info("balance the classes fraud and non-fraud classes with SMOTE basically doing oversampling")
            #doing oversampling 
            smote_obj=SMOTE(sampling_strategy='minority')

            X,y=smote_obj.fit_resample(X,y)

            #now spliting the data
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,stratify=y)

            #calling the preprocessor object
            preprocessor=self.get_data_transformation()

            X_train[["Time","Amount"]]=preprocessor.fit_transform(X_train[["Time","Amount"]])
            X_test[["Time","Amount"]]=preprocessor.transform(X_test[["Time","Amount"]])

            #now concat the array (X_train_array+y_train, X_test_array+y+test)
            train_array=np.c_[np.array(X_train),np.array(y_train)]
            test_array=np.c_[np.array(X_test),np.array(y_test)]

            #os.makedirs(os.path.dirname(self.Datatrans_config_obj.preprocessor_path))
            save_obj(
                self.Datatrans_config_obj.preprocessor_path,
                obj=preprocessor)
            return(
                train_array,
                test_array
                
                #print(self.Datatrans_config_obj.preprocessor_path)
            )
        except Exception as e:
            raise Custom_Exception(e,sys)
        
