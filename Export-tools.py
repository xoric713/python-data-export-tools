import sys,os

def copy_file(Source_path: str, dest_path: str) -> None:
    try:
        if not os.path.exists(Source_path):
            raise FileNotFoundError(f"Source File '{Source_path}' does not exist.")

        # Ensure the destination directory exists
        dest_dir = os.path.dirname(dest_path)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        with open(Source_path, 'r') as Source:
            data = Source.read()
        with open(dest_path, 'w') as Dest:
            Dest.write(data)
        print(f"Data successfully copied from {Source_path} to {dest_path}.")
    except Exception as e:
        print(f"Error Copying file: {e}")

def main(args: list) -> None:
    if len(args) < 3:
        print("Usage: python Export-tools.py <source_path> <destination_path>")
        sys.exit(1)
    source_path = args[1]
    dest_file = args[2]
    copy_file(source_path, dest_file)

if __name__ == "__main__":
    main(sys.argv)