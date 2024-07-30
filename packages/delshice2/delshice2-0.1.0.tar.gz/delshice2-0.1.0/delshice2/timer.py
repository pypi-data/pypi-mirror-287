import os
import time
import subprocess
import sys

TIMER_FILE = os.path.expanduser("~/.self_deleting_package_timer")

def create_timer():
    with open(TIMER_FILE, 'w') as f:
        f.write(str(time.time()))

def is_time_exceeded(minutes=5):
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
    package_name = "delshice2"
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package_name])
    delete_timer()
