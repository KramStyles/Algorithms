import argparse
from datetime import datetime, timedelta
import logging
from pathlib import Path

logging.basicConfig(
    filename=str(Path(__file__).resolve().parent / "cleanup.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def run(directory=None, days=30):
    if not directory:
        raise ValueError("Directory wasn't provided")
    directory = Path(directory).absolute()
    cutoff_date = datetime.now() - timedelta(days=days)

    if not directory.exists() or not directory.is_dir():
        raise ValueError("Invalid directory path!")

    logging.info("Starting cleanup script execution...")

    # Transverse through the directory
    for file_path in directory.rglob("*"):
        file_path = file_path.absolute()
        if file_path.is_file():
            # Get time file was updated
            mod_time = file_path.stat().st_mtime
            mod_time = datetime.fromtimestamp(mod_time)
            # remove file if it's less than the expected date
            if mod_time < cutoff_date:
                print(f"File to remove: {file_path} (Last modified: {mod_time})")
                file_path.unlink() # Remove the file
                logging.warning(f"Deleted file: {file_path}")

    print(directory, cutoff_date)



if __name__ == "__main__":
    try:
        # Set up parser and parser arguments.
        parser = argparse.ArgumentParser(description="Clean up old files in the given directory.")
        parser.add_argument("--directory", help="Target directory")
        parser.add_argument("--days", type=int, help="Age threshold in days")
    
        # Fetch inserted arguments
        args = parser.parse_args()
        run(args.directory, args.days)
    except (TypeError, ValueError) as err:
        logging.error(f"{err}")
