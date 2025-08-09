import subprocess
import sys
import os
import argparse
from rollback import *

def getpkg():
    parser = argparse.ArgumentParser(description="Get package name from command line")
    parser.add_argument("package", help="Name of the package")
    args = parser.parse_args()
    pkg = args.package
    return pkg