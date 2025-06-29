from setuptools import setup, find_packages
from typing import List 

def get_requirements() -> List[str]:
    """
    Function to get the list of requirements from the requirements.txt file.

    """
    requirements_list: List[str] = []

    try:
        # Open and read the requirements.txt file
        with open("requirements.txt", "r") as file:
            # Read each line in the file
            lines = file.readlines()

            # Processing each line
            for line in lines:
                # Strip whitespaces and new lines
                requirement = line.strip()

                # Ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirements_list

print(get_requirements())

setup(
    name = "AI_Trip_Planner",
    version = "0.0.1",
    author = "Smaranava Roy",
    author_email = "roy.smaranavaroy@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)


