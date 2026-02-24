#We will apply some machinelearning algorithm

import os 
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from src.mlproject.utils import save_object, evaluate_models
import numpy as np
import mlflow
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
@dataclass

class ModelTrainerConfig:
    # here we have to take the train and test dataset , and then train the model and save its pickel file(pkl) somewhere

    trained_model_file_path = os.path.join("artifacts","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
       
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    
       
    def initiate_model_trainer(self,train_array, test_array):
        try:
            logging.info("Split training and test input data")
            x_train, y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            models = {
                "Linear Regression": LinearRegression(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()
            }
            
            #Now we will do hyperparameter tuning
            
            params = {
                "Decision Tree":{
                    'criterion':['squared_error', 'friedman_mse','absolute_error','poisson'],
                    # 'splitter': ['best','random'],
                    # 'max_features : ['sqrt','log2']
                
                },
                "Random Forest" :{
                    # 'criterion' : ['squared_error', 'friedman_mse','absolute_error','poisson'],
                    # 'max_features : ['sqrt','log2','None'],
                    
                'n_estimators':[8,16,32,64,128,256]
                },
                "Gradient Boosting" : {
                    # 'loss' :['squared_error','huber','absolute_error','quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    #'criterion' : ['squared_error', 'friedman_mse'],
                    # 'max_features : ['sqrt','log2','auto'],
                    'n_estimators':[8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                 'learning_rate':[.1,.01,.05,.001],  
                 'n_estimators':[8,16,32,64,128,256] 
                },
                "CatBoosting Regressor":{
                    'depth':[6,8,10],
                    'learning_rate':[.1,.01,.05,.001],
                    'iterations':[30,50,100]
                },
                "AdaBoost Regressor":{
                  'learning_rate':[.1,.01,.05,.001],
                  # 'loss' : ['linear','square','exponential'],
                   'n_estimators':[8,16,32,64,128,256] 
                }
            }
            model_report:dict= evaluate_models(x_train,y_train,x_test,y_test,models,params)
            
            ## To get the best model score form the dictionary
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]   
            best_model = models[best_model_name]
            
            print("This is the best Model")
            print(best_model_name)
            
            model_names = list(params.keys())
            
            actual_model ="" #initially or actual model is blank and the we  update it
            
            for model in model_names:
                if best_model_name == model:
                    actual_model = actual_model+ model
            
            best_params = params[actual_model]
            
            # we are pasting the dagshub url here
            
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            
            with mlflow.start_run(): #we are starteing likt this way
                
                predicted_qualities = best_model.predict(x_test)
                
                (rmse,mae,r2) = self.eval_metrics(y_test, predicted_qualities)
                
                mlflow.log_params(best_params)
                
                mlflow.log_metric('rmse',rmse)
                mlflow.log_metric('mae', mae)
                mlflow.log_metric('r2', r2)

                #Model registry does not work with file store
                
                if tracking_url_type_store != 'file':
                    mlflow.sklearn.log_model(best_model, 'model', registered_model_name=actual_model)
                else:
                    mlflow.sklearn.log_model(best_model, 'model')
            #this is saved in pickle file if the r2 score is greater than 60%
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            ) 
           
            predicted = best_model.predict(x_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square 
            
                
        except Exception as e:
            raise CustomException(e,sys)