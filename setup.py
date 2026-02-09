from setuptools import find_packages,setup

HYPEN_E_DOT = "-e ."
# find_packages maps application structure and make folders as a packages

#making a function that automatically get the packages that we have in requirements.txt file
def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) #So to directly execute the setup .py file we use this hypen dot key varaible stored value in requirements , so here to ignore that whille egtthing the neccesary packages , we need to ignore that
    return requirements 
    


setup(
name = "mlproject",
version = "0.0.1",
author = "nishita",
author_email = "nishitaagrawak28608@gmail.com",
packages = find_packages(), #it will automatically find
install_requires= get_requirements("requirements.txt")#whatever basic ibraries that we need ti install

)
## after running this our appplication will become like a package 
