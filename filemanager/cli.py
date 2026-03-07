import argparse
import sys
from filemanager.fs_manager import copy_file, delete_path, count_files, search_files, add_creation_date, analyze_sizes

def main():
    parser = argparse.ArgumentParser(description="File System Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    try:

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()