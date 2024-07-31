from setuptools import setup, find_packages

with open("README.md", "r") as file:
    description = file.read()

setup(
    name='simple-telegram-api',        # Name of your package
    version='0.1.5',            # Version of your package
    packages=find_packages(), # Automatically find packages
    install_requires=[],      # List of dependencies
    long_description=description,
    long_description_content_type="text/markdown",
)
