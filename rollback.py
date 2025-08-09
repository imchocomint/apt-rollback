import subprocess
import sys
import os
import argparse
from getpkginp import *


def getpkgvr(pkg):
    gvc = f"apt-cache showpkg {pkg} | grep -o '^[0-9]\\+\\.[0-9]\\+\\.[0-9]\\+-[0-9]\\+' | head -n 2"
    get_cur = f"apt list {pkg} | grep installed | grep -oP '\\d+\\.\\d+\\.\\d+-\\d+'"
    gov_get = "| sed -n '2p'"
    version = subprocess.run(gvc, shell=True, capture_output=True, text=True, check=True)
    print("These versions are available:")
    print(version.stdout.strip())
    insv = subprocess.run(get_cur, shell=True, capture_output=True, text=True, check=True)
    print("Currently installed version:")
    print(insv.stdout.strip())
    print("If you downgrade, the package version will be:")
    dver_cmd = f"{gvc} {gov_get}"
    dver = subprocess.run(dver_cmd, shell=True, capture_output=True, text=True, check=True)
    print(dver.stdout.strip())
    return version.stdout.strip(), insv.stdout.strip(), dver.stdout.strip()

def rollback(pkg,dver):
    rollback_cmd = f"sudo apt-get install {pkg}={dver}"
    print(f"Rolling back {pkg} to the previous version...")
    try:
        subprocess.run(rollback_cmd, shell=True, check=True)
        print(f"Successfully rolled back {pkg} to version {dver}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to roll back {pkg}: {e}")
        sys.exit(1)
