from setuptools import find_packages, setup
from typing import List


# Constant that triggers the setup.py file
HYPEN_E_DOT = '-e .'

# Get requirements to install
def get_requirements(file_path: str) -> List[str]:

    """
    Extract requirements from a requirements file.
    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of requirements extracted from the file.
    """

    requirements = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and comments
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Append requirement to list
            requirements.append(line)

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='niazroky',
    author_email='niazroky75@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


