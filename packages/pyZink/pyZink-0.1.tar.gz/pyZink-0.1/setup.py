from setuptools import setup, find_packages

def parse_requirements(filename: str = "requirements.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line and not line.startswith("#")]

def parse_readme(filename: str = "README.md"):
        with open(filename, 'r', encoding='utf-8') as fh:
            return fh.read()

setup(
    name="pyZink",
    version="0.1",
    description='Python functionality that I use on a regular basis, that others might find use or inspiration from.',
    long_description=parse_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Peasniped/pyZink',
    author='Cernott',
    author_email='pyZink@znk.dk',
    packages=find_packages(),
    install_requires=parse_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)