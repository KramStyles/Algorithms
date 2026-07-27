import argparse
import logging
import os

def run():
    # Set up parser and parser arguments.
    parser = argparse.ArgumentParser(description="Clean up old files in the given directory.")
    parser.add_argument("--directory", help="Target directory")
    parser.add_argument("--days", type=int, default=30, help="Age threshold in days")

    # Fetch inserted arguments
    args = parser.parse_args()
    directory = args.directory
    days = args.days
    print(f"Target: {args.directory}, Days: {args.days}")



if __name__ == "__main__":
    run()
