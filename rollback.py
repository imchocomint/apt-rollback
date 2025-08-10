import subprocess
import sys
import os
import argparse
from getpkginp import *

def getpkgvr(pkg_name, mode=None):
    gvc = f"apt-cache showpkg_name {pkg_name} | grep -o '^[0-9]\\+\\.[0-9]\\+\\.[0-9]\\+-[0-9]\\+' | head -n 2"
    get_cur = f"apt list {pkg_name} | grep installed | grep -oP '\\d+\\.\\d+\\.\\d+-\\d+'"
    gov_get = "| sed -n '2p'"
    dver_cmd = f"{gvc} {gov_get}"
    version = subprocess.run(gvc, shell=True, capture_output=True, text=True, check=True)
    insv = subprocess.run(get_cur, shell=True, capture_output=True, text=True, check=True)
    dver = subprocess.run(dver_cmd, shell=True, capture_output=True, text=True, check=True)
    if mode == "pp" or mode == "unpp":
        print("Currently installed version:")
        print(insv.stdout.strip())
    else:
        print("These versions are available:")
        print(version.stdout.strip())
        print("Currently installed version:")
        print(insv.stdout.strip())
        print("If you downgrade, the package version will be:")
        print(dver.stdout.strip())
    return version.stdout.strip(), insv.stdout.strip(), dver.stdout.strip()

def rollback(pkg_name,dver):
    rollback_cmd = f"sudo apt-get install {pkg_name}={dver}"
    print(f"Rolling back {pkg_name} to the previous version...")
    try:
        subprocess.run(rollback_cmd, shell=True, check=True)
        print(f"Successfully rolled back {pkg_name} to version {dver}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to roll back {pkg_name}: {e}")
        sys.exit(1)

def pinpkg(pkg_name, insv):
    hold_cmd = f"sudo apt-mark hold {pkg_name}"
    print(f"Pinning version {insv} of {pkg_name}...")
    try:
        subprocess.run(hold_cmd, shell=True, check=True)
        print(f"{pkg_name} is now held and will not be upgraded.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to hold {pkg_name}: {e}")
        sys.exit(1)

def unpinpkg(pkg_name, insv):
    unhold_cmd = f"sudo apt-mark unhold {pkg_name}"
    print(f"Unpinning version {insv} of {pkg_name}...")
    try:
        subprocess.run(unhold_cmd, shell=True, check=True)
        print(f"{pkg_name} is now unheld and can be upgraded.")
        print("Do you want to upgrade this package? (y/n)")
        unpinres = input().strip().lower()
        if unpinres == 'y':
            upgrade_cmd = f"sudo apt-get install {pkg_name}"
            subprocess.run(upgrade_cmd, shell=True, check=True)
            print(f"{pkg_name} has been upgraded.")
        else:
            print(f"You decided not to upgrade {pkg_name} for now.")
            sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"Failed to unhold {pkg_name}: {e}")
        sys.exit(1)