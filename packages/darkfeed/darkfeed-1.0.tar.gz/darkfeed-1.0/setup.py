from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        README = f.read()
    return README

setup(
    name="darkfeed",
    version="1.0",
    author="Camila Santiago",
    description="A CLI parser for data from Dark Feed",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires = ['python-dateutil','requests', 'openpyxl', 'Flask'],
    keywords= ['ransomware', 'victims', 'darkfeed', 'dark feed'],
    entry_points={
        "console_scripts": [ "darkfeed = darkfeed.main:main"],
    },
)