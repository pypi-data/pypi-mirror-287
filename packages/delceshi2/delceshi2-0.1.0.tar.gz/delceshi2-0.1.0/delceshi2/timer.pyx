# timer.pyx
import os
import time
import subprocess
import sys

TIMER_FILE = os.path.expanduser("~/.self_deleting_package_timer")

def create_timer():
    with open(TIMER_FILE, 'w') as f:
        f.write(str(time.time()))

def is_time_exceeded(double minutes=3):
    if not os.path.exists(TIMER_FILE):
        return False
    with open(TIMER_FILE, 'r') as f:
        install_time = float(f.read())
    current_time = time.time()
    return (current_time - install_time) > (minutes * 60)

def delete_timer():
    if os.path.exists(TIMER_FILE):
        os.remove(TIMER_FILE)

def uninstall_package():
    package_name = "self_deleting_package"
    try:
        # Check if the package is installed
        installed = subprocess.check_output([sys.executable, "-m", "pip", "show", package_name]).decode()
        if installed:
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package_name])
        delete_timer()
    except subprocess.CalledProcessError:
        pass
