import os,sys
from pathlib import Path
import pandas as pd
import numpy as np

#some local packages
from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.Utils import load_obj

class Prediction_Pipeline:
    def __init__(self):
        pass

    def initiate_prediction(self,data_frame):
        try:
            model_path=Path(os.path.join("artifacts","model.pkl"))
            model=load_obj(model_path)
            #loading the preprocessor for getting transformation
            preprocessor_path=Path(os.path.join("artifacts","preprocessor.pkl"))
            preprocessor=load_obj(preprocessor_path)
            #now transform the data 
            data_frame[["Time","Amount"]]=preprocessor.transform(data_frame[["Time","Amount"]])

            #data is ready to predit the result

            predict_data=model.predict(data_frame)

            return predict_data

        except Exception as e:
            raise Custom_Exception(e,sys)
        

class Custom_data:
    def __init__(self,Time:float,
                 v1:float,
                 v2:float,
                 v3:float,
                 v4:float,
                 v5:float,
                 v6:float,
                 v7:float,
                 v8:float,
                 v9:float,
                 v10:float,
                 v11:float,
                 v12:float,
                 v13:float,
                 v14:float,
                 v15:float,
                 v16:float,
                 v17:float,
                 v18:float,
                 v19:float,
                 v20:float,
                 v21:float,
                 v22:float,
                 v23:float,
                 v24:float,
                 v25:float,
                 v26:float,
                 v27:float,
                 v28:float,
                 Amount:float,
                 ):
        self.Time=Time
        self.V1=v1
        self.V2=v2
        self.V3=v3
        self.V4=v4
        self.V5=v5
        self.V6=v6
        self.V7=v7
        self.V8=v8
        self.V9=v9
        self.V10=v10
        self.V11=v11
        self.V12=v12
        self.V13=v13
        self.V14=v14
        self.V15=v15
        self.V16=v16
        self.V17=v17
        self.V18=v18
        self.V19=v19
        self.V20=v20
        self.V21=v21
        self.V22=v22
        self.V23=v23
        self.V24=v24
        self.V25=v25
        self.V26=v26
        self.V27=v27
        self.V28=v28
        self.Amount=Amount


        

    def initiate_data(self):
        try:
            #here we make a Data_Frame 
            Columns_names=["Time","V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"]
            data=[ self.Time,self.V1,self.V2,self.V3,self.V4,self.V5,self.V6,self.V7,self.V8,self.V9,self.V10,self.V11,self.V12,self.V13,self.V14,self.V15,self.V16,self.V17,self.V18,self.V19,self.V20,self.V21,self.V22,self.V23,self.V24,self.V25,self.V26,self.V27,self.V28,self.Amount]

            data_frame=pd.DataFrame(data=[data],columns=Columns_names)
            logging.info(f"the data is feed:\n {data_frame.head()} ")

            return data_frame
        except Exception as e:
            raise Custom_Exception(e,sys)