import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# this is basically current time specify karega , in format of month, data, year, hour, min , sec in .log named file
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# We are creating log file path, in this we get current working directory and its will be saved  as logs folder and log file will be saved in this.
os.makedirs(log_path,exist_ok = True)
# folder of log path

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)
# this iwll combine path and file name

# format of logging message
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #time, line no. ,name, level name, message of error or message to be displayed
    level = logging.INFO # this different level, error can also be written or warning)
)