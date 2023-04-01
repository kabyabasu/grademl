from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str)-> List[str]:

    '''
    This function will return the list of the requiremnts
    '''

    req = []

    with open(file_path) as f:

        req = f.readlines()
        req = [n.replace('\n','')for n in req]

        if "-e ." in req:
            req.remove("-e .")

    return req



        


setup(
    name= 'gradeML',
    version = '0.0.1',
    author='kabyabasu',
    author_email='kabyabasu@gmail.com',
    packages=find_packages(),
    requires= get_requirement('requirements.txt')


)