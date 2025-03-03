"""
    download.py

    Tools for use in a Jupyter Notebook for Data Analysis.
"""

from cmd import Cmd
from glob import glob
import hashlib
import logging
import os
from pathlib import Path
import pickle
import re
import shutil
import sys
import time
from urllib.parse import urlparse
import warnings
from zipfile import ZipFile

from bs4 import BeautifulSoup as BS
from chromedriver_py import binary_path
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

TESTING = True
VERBOSE = True
RUNNING_IN_JUPYTER = Path(sys.argv[0]).stem.startswith('ipykernel')
RUNNING_CLI = not RUNNING_IN_JUPYTER

if RUNNING_IN_JUPYTER:
    try:
        import ipynbname
        nb_path = ipynbname.path()
        PROJECT_DIR = nb_path.parent
    except FileNotFoundError:
        print("Can't find the notebook name. Are you running this in a notebook?")
else:
    PROJECT_DIR = Path(pwd()).parent.parent

PROJECT_DIR
DATA_LAB_DIR = Path(__file__).parent.parent
PROJECT_NAME = PROJECT_DIR.name
DATA_DIR = DATA_LAB_DIR / 'data' / PROJECT_NAME
TEST_DIR = DATA_LAB_DIR / 'test' / PROJECT_NAME
ARCHIVE = DATA_LAB_DIR / 'archive' / PROJECT_NAME
CLEAN_DIR = DATA_LAB_DIR / 'clean' / PROJECT_NAME
STAGED_DIR = DATA_LAB_DIR / 'staged' / PROJECT_NAME
DOWNLOAD = DATA_LAB_DIR / 'download' / PROJECT_NAME
CACHE_PATH = DATA_LAB_DIR / 'cache' / PROJECT_NAME / f'{PROJECT_NAME.split('-')[0]}.pkl'
CACHE_FILE = str(DATA_LAB_DIR / 'cache' / f'{PROJECT_NAME}.pkl')

