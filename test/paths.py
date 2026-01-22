from pathlib import Path
folder = Path(".")
for item in folder.iterdir():
  print(item)

from pathlib import Path
hold = Path("C:/Users/user")
for object in hold.iterdir():
 if object.is_file():
   print("File name:",object.name)
 elif object.is_dir():
   print("Dir name:",object.name)

from pathlib import Path
files=Path("C:/Users/user")
for band in files.iterdir():
  stats=band.stat()
  size=stats.st_size
  print(band)
  print(size)

import argparse
from pathlib import Path

parser= argparse.ArgumentParser()
parser.add_argument("directory",type=str, help="directory path to scan")

args = parser.parse_args()

folder = Path(args.directory)

if folder.exists() and folder.is_dir():
    for item in folder.iterdir():
        if item.is_file():
            print(f"[FILE] {item.name}")
        elif item.is_dir():
            print(f"[DIR ] {item.name}")
else:
    print(f"Error: {args.directory} is not a valid directory")

 