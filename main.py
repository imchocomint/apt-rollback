import subprocess
import sys
import os
import argparse

from rollback import *
from getpkginp import *

print("Welcome to apt-rollback.")
print("You've decided to rollback package {pkg}.")
pkg = getpkg()
version, installed_version, downgrade_version = getpkgvr(pkg)
print("Do you want to downgrade this package? (y/n)")
response = input().strip().lower()
if response == 'y':
    rollback(pkg, downgrade_version)
else:
    print("You decided not to rollback {pkg}.")
    sys.exit(0)