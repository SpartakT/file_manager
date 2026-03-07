import os
import shutil
import re
import time

def copy_file(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} not found")
    shutil.copy(source, destination)

def delete_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)