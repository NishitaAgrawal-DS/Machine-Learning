#custom exception
import sys 
from src.mlproject.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # this bring three info
    if exc_tb is None:
        return f"Error message: {str(error)}"
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    # here 0 will be replaced by file name, 1 by line number, error message by 2

class CustomException(Exception):
    def __init__(self,error_message, error_details:sys): #initializer of the class that we created
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
        
    def __str__(self):
        return self.error_message