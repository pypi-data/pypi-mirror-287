import os
import subprocess
import requests
import sys
import argparse
import platform
from packaging import version

"""Note: use Astris from Crystal train to work with baseband KIS, not LuckFennel
sudo green-restore -i CurrentCrystal
knox home-diag Crystal22A309 (if green-restore doesn't allow you to downgrade HD)
"""


def macOS_ver():
    return platform.mac_ver()[0]


def lldb_ver():
    try:
        result = subprocess.run(['lldb', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.stdout.decode('utf-8')
    except FileNotFoundError:
        return "LLDB Not Found"


def homeDiagnostic_ver():
    try:
        result = subprocess.run(['knox', 'home-diag', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return result.stdout.decode('utf-8')
    except FileNotFoundError:
        return "Home Diagnostic Not Found"


# Fix this to get the latest bin file from the Chimp Documentation website. Currently the latest version is 1.28
def updateChimpFirmware():
    serialnumber = input("Enter Chimp Cable Serial Number:")
    update_command = f"astrisctl --host ChimpSWD-{serialnumber} fwupdate /Users/smartlab/shree_kumar/ChimpFirmware/1.27/Chimp-0127.bin"

    print(f"Updating the firmware for Chimp Cable")
    try:
        subprocess.run(update_command, shell=True, check=True)
    except:
        print(f"Error updating the firmware")


def updateMacOS():
    print("Checking for MacOS Updates")
    try:
        result = subprocess.run(['softwareupdate', '-l'], check=True, text=True)
        if "No new software is available." in result.stdout:
            print("macOS up tp date.")
        else:
            print("macOS update available. Starting update...")
            subprocess.run(['sudo', 'softwareupdate', '-i', '-a'], check=True, text=True)
    except subprocess.CalledProcessError:
        print("macOS update failed")


def update_LLDB():
    print("Checking for LLDB Updates")
    try:
        subprocess.run(['xcode-select', '--install'], check=True)
        print("lldb update successful")
    except subprocess.CalledProcessError:
        print("lldb update failed")


def updateHomeDiagnostic():
    print("Updating Home Diagnostic")
    try:
        result = subprocess.run(['knox', 'home-diag', 'CurrentLuckFennel'], check=True)
    except subprocess.CalledProcessError:
        print("Home Diagnostic update failed")


def display_versions():
    print("Installed Software versions")
    print(f"macOS Version: {macOS_ver()}")
    print(f"lldb Version: {lldb_ver()}")
    print(f"Home Diagnostic Version: {homeDiagnostic_ver()}")


def main():
    parser = argparse.ArgumentParser("Baseband Bring Up Automation Setup Tool")
    parser.add_argument("-v", "--version", action='store_true', help="Display the versions of all installed softwares")
    ###Add in a help argument to explain about the setup Phase

    # parser.add_argument('--force-update', action="store_true", help='Update All Softwares without User Intervention')
    # parser.add_argument('--skip-checks', action="store_true", help='Skip Checks for this version')

    args = parser.parse_args()

    if args.version:
        display_versions()
    else:
        display_versions()
        print("Which software do you want to update?")
        print(f"1. MacOS")
        print(f"2. lldb")
        print(f"3. Home Diagnostic")
        print(f"4. Chimp Firmware")
        print("Enter the numbers (comma-separated) or 'all' to update everything")
        choice = input("Choice: ").strip().lower()
        if choice == "all":
            updateMacOS()
            update_LLDB()
            updateHomeDiagnostic()
            updateChimpFirmware()
        else:
            choices = [int(c.strip()) for c in choice.split(",") if c.strip().isdigit()]
            if 1 in choices:
                updateMacOS()
            if 2 in choices:
                update_LLDB()
            if 3 in choices:
                updateHomeDiagnostic()
            if 4 in choices:
                updateChimpFirmware()

        print("Update process complete")


if __name__ == "__main__":
    main()
