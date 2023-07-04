from pathlib import Path
import shutil
import sys
from normalize import normalize
import file_parser as parser

def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder:Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ""))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()))
    except shutil.ReadError as e:
        print(f"It's not archive, Error is: {e}")
        folder_for_file.rmdir()
        return None
    filename.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print("Error during remove file!")

def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / "images" / "JPEG" )
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / "images" / "JPG" )
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / "images" / "PNG" )
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / "images" / "SVG" )
    for file in parser.MY_OTHER:
        handle_media(file, folder / "MY_OTHER" )
    for file in parser.ARCHIVES:
        handle_media(file, folder / "archives" )

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)
