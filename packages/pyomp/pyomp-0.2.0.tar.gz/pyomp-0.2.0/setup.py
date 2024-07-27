from setuptools import setup, find_packages
setup(
name='pyomp',
version='0.2.0',
author='Todd A. Anderson',
author_email='todd.a.anderson@intel.com',
description='A placeholder and redirector to the conda install for pyomp.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)
