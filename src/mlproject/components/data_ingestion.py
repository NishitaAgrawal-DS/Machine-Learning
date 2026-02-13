## MySql---> Train test split ----> dataset
import os #for current path 
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd  
from src.mlproject.utils import read_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


# This will help to initiallise imnput parameters 

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    # this will give us the path to save our data path 
    #artifact path is used to save the data ingestion output
    
class DataIngestion :
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    ## Here we have initial configuration from data conf class which will have all 3 paths from above
    
    
    def initiate_data_ingestion(self):
        try:
            ##reading code from the sql
            df = read_sql_data()
            #here my dataframe is here and this is my raw data
        
            logging.info("Reading completed MySQL database")
            #after reading the data frame that we hvae will be save in raw data path, we will amke artifact folder
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            #when this code will run our atifact folder will be ctreated immediately

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            
            #This is the raw data which is gonna be train and split

            train_set,test_set = train_test_split(df,test_size = 0.2, random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("Data Ingestion is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys) # tray catch block implementation
        