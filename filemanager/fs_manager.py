import os
import shutil
import re
import time

def copy_file(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} not found")
    shutil.copy(source, destination)