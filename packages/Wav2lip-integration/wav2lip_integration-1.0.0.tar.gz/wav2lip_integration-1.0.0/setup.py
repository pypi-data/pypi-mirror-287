#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

MAJOR =1
MINOR =0
PATCH =0
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"

def get_install_requires():
    reqs = [
        'pandas',
        'numpy',
        'librosa',
        'pyaudio==0.2.14',
        'opencv-python',
        'torch',
        'tqdm',
        'numba',
        'setuptools',
        'flask==3.0.3',
        'openvino==2024.1.0',
        'batch-face==1.4.0',
        'watchdog==4.0.0'

    ]
    return reqs
setup(
	name = "Wav2lip_integration",
	version = VERSION,
    author ="Kevin3777",
    author_email = "wyj3777@outlook.com",
    long_description_content_type="text/markdown",
	#url = 'https://github.com/songroom2016/dbpystream.git',
	#long_description = open('README.md',encoding="utf-8").read(),
    python_requires=">=3.6",
    install_requires=get_install_requires(),
	packages = find_packages(),
 	license = 'Apache',
   	classifiers = [
       'License :: OSI Approved :: Apache Software License',
       'Natural Language :: English',
       'Operating System :: OS Independent',
       'Programming Language :: Python',
       'Programming Language :: Python :: 3.6',
       'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_data={'': ['*.csv', '*.txt','.toml']}, #这个很重要
    include_package_data=True #也选上

)
