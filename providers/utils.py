import argparse
import os
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=Path, help="entry filename")
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        parser.error("The provided file does not exist")

    return args
