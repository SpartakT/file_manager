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

    count_parser = subparsers.add_parser("count", help="Count files in folder (including subfolders)")
    count_parser.add_argument("path", nargs="?", default=".", help="Path (default: current dir)")

    search_parser = subparsers.add_parser("search", help="Search files by regex in folder (including subfolders)")
    search_parser.add_argument("path", nargs="?", default=".", help="Path (default: current dir)")
    search_parser.add_argument("pattern", help="Regex pattern")

    add_date_parser = subparsers.add_parser("add_date", help="Add creation date to file/folder names")
    add_date_parser.add_argument("path", help="File or folder")
    add_date_parser.add_argument("--recursive", action="store_true", help="Recursive for subfolders")

    analyse_parser = subparsers.add_parser("analyse", help="Analyze sizes in folder")
    analyse_parser.add_argument("path", nargs="?", default=".", help="Path (default: current dir)")

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
        elif args.command == "count":
            count = count_files(args.path)
            print(f"Total files: {count}")
        elif args.command == "search":
            results = search_files(args.path, args.pattern)
            print("Found files:")
            for res in results:
                print(res)
        elif args.command == "add_date":
            add_creation_date(args.path, args.recursive)
            print(f"Added dates to files in {args.path} (recursive: {args.recursive})")
        elif args.command == "analyse":
            analyze_sizes(args.path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()