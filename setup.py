from setuptools import find_packages,setup
from typing import List

HYPHEN = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''gets the reqirements from the path of a file'''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)

    return requirements

setup(
    name = 'practice_project1',
    version='0.0.1',
    author='chetanaananda',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)