import subprocess
import sys
import os
import argparse

from rollback import *
from getpkginp import *

def getmode():
    parser = argparse.ArgumentParser(description="Pin/unpin/rollback a package")
    parser.add_argument("mode", choices=["pp", "unpp"], help="Mode to set for the package")
    parser.add_argument("pkg", help="Package name to operate on")
    return parser.parse_args()


def dgcmd(pkg, downgrade_version):
    print(f"You've decided to rollback package {pkg}.")
    print("Do you want to downgrade this package? (y/n)")
    response = input().strip().lower()
    if response == 'y':
        rollback(pkg, downgrade_version)
    else:
        print(f"You decided not to rollback {pkg}.")
        sys.exit(0)



if __name__ == "__main__":
    args = getmode()
    pkg = getpkg(args.pkg)
    print("Welcome to apt-rollback.")
    if args.mode == "pp":
        _, installed_version, _ = getpkgvr(pkg, mode="pp")
        pinpkg(pkg, installed_version)
    elif args.mode == "unpp":
        _, installed_version, _ = getpkgvr(pkg, mode="unpp")
        unpinpkg(pkg, installed_version)
    else:
        version, installed_version, downgrade_version = getpkgvr(pkg)
        dgcmd(pkg, downgrade_version)


