from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

if __name__ == "__main__": #execution point of the file to check
    logging.info("The executon has started")
        
    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)