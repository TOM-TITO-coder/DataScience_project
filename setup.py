from typing import List
from setuptools import setup, find_packages

HYPEN_E_DOT ='-e .'

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''
    
    requirements = []
    with open('requirements.txt') as file_obje:
        requirements = file_obje.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.1',
    author='Tito',
    author_email='titotom934@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)