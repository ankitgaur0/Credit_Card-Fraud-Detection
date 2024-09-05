import os,sys
import pandas as pd
import numpy as np
from pathlib import Path
from dataclasses import dataclass
#package for getting url
from urllib.parse import urlparse
#some local packages
from src.Logger import logging
from src.Exception_handler import Custom_Exception
from src.Utils import save_obj

#some built in packages to evaluating the models
import mlflow
import mlflow.keras
from sklearn.metrics import classification_report,accuracy_score


@dataclass
class Best_Model_Config:
    best_model_path :str=os.path.join("artifacts","model.pkl")

class Model_Evaluation:
    def __init_(self):
        self.best_model_path_obj=Best_Model_Config()
    
    def get_evaluation_metrics(self,actual_data,predict_data):
        try:
            accuracy=accuracy_score(actual_data,predict_data)
            classifcation_report={}
            classification_report=classification_report(actual_data,predict_data)


            return (accuracy,classifcation_report)
        except Exception as e:
            raise Custom_Exception(e,sys)

    def initiate_evaluation(self,test_array,models_dict:dict,svc_best_parm):
        try:
            logging.info("Model Evaluation is starting")
            X_test_array=test_array[:,:-1]
            y_test_array=test_array[:,:-1]

            mlflow.set_registry_uri("https://dagshub.com/ankitgaur0/Credit_Card-Fraud-Detection.mlflow")
            tracking_url_store=urlparse(mlflow.get_artifact_uri()).scheme

            logging.info("starting the mlflow")
            with mlflow.start_run():
                model_meritcs={}
                for model_name ,model in models_dict.items():
                    if model_name !="Support Vector Classifier":
                        predict_data=model.predict(X_test_array)
                        (accuracy,classification_report)=self.get_evaluation_metrics(y_test_array,predict_data)
                        mlflow.log_metric(f"{model_name} accuracy report",accuracy)

                        for class_lable,metrics in classification_report.items():
                            if class_lable not in ["accuracy","macro avg","weighted avg"]:
                                for metrics_name,metrics_value in metrics.items():
                                    mlflow.log_metric(f"{class_lable}_{metrics_name }",metrics_value)
                                    logging.info(f"{class_lable}_{metrics_name} :{metrics_value}")
                        model_meritcs[model_name]=accuracy

                    else:
                        predict_data=model.predict(X_test_array)
                        (accuracy,classification_report)=self.get_evaluation_metrics(y_test_array,predict_data)
                        mlflow.log_metric(f"{model_name} accuracy_score ",accuracy)

                        for class_lable,metrics in classification_report.items():
                            if class_lable not in ["accuracy","macro avg","weighted avg"]:
                                for metrics_name,metrics_value in metrics.items():
                                    mlflow.log.metics(f"{class_lable}_{metrics_name}",metrics_value)
                                    logging.info(f"{class_lable}_{metrics_name} :{metrics_value}")
                                    mlflow.log_metrics("best_parameter for the svc",svc_best_parm)
                        model_meritcs[model_name]=accuracy
                   
                

                
                if model_meritcs["logistic_regression"] > model_meritcs["Support Vector Classifier"]:
                    best_model=models_dict["logistic_regression"]
                else:
                    best_model=models_dict["Support Vector Classifier"]
                if tracking_url_store !="file": 
                    mlflow.keras.load_model(best_model,"sklearn model",registered_model_name="sklearn_model")

                else:
                    mlflow.keras.log_model(best_model,"model")

            

            save_obj(self.best_model_path_obj.best_model_path,
                     obj=best_model)   



            

        except Exception as e:
            raise Custom_Exception(e,sys)