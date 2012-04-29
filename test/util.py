
import sys
import os.path

# Import various testing utils
from utils import *

def modImportPath():
    myDir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(os.path.abspath(myDir), '..', 'src'))

modImportPath()

