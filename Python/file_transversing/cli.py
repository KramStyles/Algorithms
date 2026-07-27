import argparse
from datetime import datetime, timedelta
import logging
from pathlib import Path

logging.basicConfig(
    filename="cleanup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def run():
    # Set up parser and parser arguments.
    parser = argparse.ArgumentParser(description="Clean up old files in the given directory.")
    parser.add_argument("--directory", help="Target directory")
    parser.add_argument("--days", type=int, default=30, help="Age threshold in days")

    # Fetch inserted arguments
    args = parser.parse_args()
    directory = Path(args.directory)
    cutoff_date = datetime.now() - timedelta(args.days)

    if not directory.exists() or not directory.is_dir():
        raise ValueError("Invalid directory path!")

    logging.info("Starting cleanup script execution...")

    # Transverse through the directory
    for file_path in directory.rglob("*"):
        if file_path.is_file():
            # Get time file was updated
            mod_time = file_path.stat().st_mtime
            mod_time = datetime.fromtimestamp(mod_time)
            # remove file if it's less than the expected date
            print(mod_time < cutoff_date)
            if mod_time < cutoff_date:
                print(f"File to remove: {file_path} (Last modified: {mod_time})")
                file_path.unlink() # Remove the file
                logging.warning(f"Deleted file: {file_path}")

    print(directory.absolute(), cutoff_date)



if __name__ == "__main__":
    run()
