#reading from the data from sql is created here
import os #for current path 
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("db_host")
user = os.getenv("db_user")
password = os.getenv("db_password")
db = os.getenv('db_name')


#this is for generic functionality

def read_sql_data():
    #paramter is from .env it is a generic functionalility
    logging.info("Reading SQL Database started")
    try:
        mydb=pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection Established: %s", mydb)

        df = pd.read_sql_query('Select * from studentdata',mydb) #we give our query and db connection
        print(df.head())
        
        return df
    
    
    
    except Exception as ex:
        raise CustomException(ex, sys)
    