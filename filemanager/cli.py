import argparse
import sys
from filemanager.fs_manager import copy_file, delete_path, count_files, search_files, add_creation_date, analyze_sizes

def main():
    parser = argparse.ArgumentParser(description="File System Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    copy_parser = subparsers.add_parser("copy", help="Copy a file")
    copy_parser.add_argument("source", help="Source file")
    copy_parser.add_argument("destination", nargs="?", default=None, help="Destination (optional, defaults to current dir)")

    delete_parser = subparsers.add_parser("delete", help="Delete a file or folder")
    delete_parser.add_argument("path", help="Path to delete")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    try:
        if args.command == "copy":
            destination = args.destination or args.source + "_copy"
            copy_file(args.source, destination)
            print(f"Copied {args.source} to {destination}")
        elif args.command == "delete":
            delete_path(args.path)
            print(f"Deleted {args.path}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()