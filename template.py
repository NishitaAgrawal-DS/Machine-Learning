## Manual (generic for every project) way to make a folder structure , we also have a automated tool available for it called as cookie cutter
import os # generic code(path) for current working directory
from pathlib import Path    #it makes our path       
import logging 

logging.basicConfig(level = logging.INFO) # we just want login info here for basic knowlege

project_name = "mlproject" #project nae can be given here

list_of_files = [
    #".github/workflows/.gitkeep", #here we are gonna make a github folder which is gona used for deployment purpose
    f"src/{project_name}/__init__.py", # here we wanna make a folder with source file inside that we have project name and it should always habe init folder
    f"src/{project_name}/components/__init__.py", #here we have all the components of training pipeline of a ml project
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py", # this will make it as a package when we compile it
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    
]

# this is for creatig the files thta are listed above to make a structure of a project more cleaner
for filepath in list_of_files:
    filepath = Path(filepath) # gives us project relative path
    filedir, filename = os.path.split(filepath)
    
    if filedir != "": 
        os.makedirs(filedir, exist_ok = True) # we will make directory
        logging.info(f"Creating Directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
            
    else:
        logging.info(f"{filename} already exists")
        
        
# The code in this file helps to create a systematic template for thr project to maintain its perfect structure

# if we need more files we can just add it in list of files and do python templat.py in terminal
