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

def count_files(path):
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} is not a directory")
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files)
    return count

def search_files(path, pattern):
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} is not a directory")
    results = []
    regex = re.compile(pattern)
    for root, dirs, files in os.walk(path):
        for file in files:
            if regex.search(file):
                results.append(os.path.join(root, file))
    return results

def add_creation_date(path, recursive=False):
    if os.path.isfile(path):
        _add_date_to_file(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path) if recursive else [(path, [], os.listdir(path))]:
            for file in files:
                if os.path.isfile(os.path.join(root, file)):
                    _add_date_to_file(os.path.join(root, file))
    else:
        raise FileNotFoundError(f"{path} not found")

def _add_date_to_file(file_path):
    ctime = os.path.getctime(file_path)
    date_str = time.strftime("%Y-%m-%d_", time.localtime(ctime))
    dir_name, file_name = os.path.split(file_path)
    new_name = os.path.join(dir_name, date_str + file_name)
    os.rename(file_path, new_name)

def analyze_sizes(path):
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} is not a directory")
    total_size = 0
    print(f"Analyzing {path}:")
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            total_size += size
            print(f"- {file_path} {human_readable_size(size)}")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_dir_size(dir_path)
            total_size += dir_size
            print(f"- {dir_path} {human_readable_size(dir_size)}")
    print(f"> full size: {human_readable_size(total_size)}")

def get_dir_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            total += os.path.getsize(os.path.join(root, file))
    return total

def human_readable_size(size):
    for unit in ['', 'kb', 'mb', 'gb', 'tb']:
        if size < 1024:
            return f"{size:.0f}{unit}"
        size /= 1024
    return f"{size:.0f}pb"