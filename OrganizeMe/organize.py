# organizing directories by categories
# this script have to located in top of organized directory
import os
from pathlib import Path

SUBDIRECTORIES = {                                          # Dictionary for filetypes
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


# Determine which folder file located based on file suffixes
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():       # iterate items in dictionary
        for suffix in suffixes:                             # return a categiry based on suffix
            if suffix == value:
                return category
    return 'MISC'                                           # return unknown suffix


def organizeDirectory():
    for item in os.scandir():                               # os.scandir grab all items in a folder
        if item.is_dir():                                   # skip the item if its a directory
            continue
        # get the file path using Path function
        filePath = Path(item)
        filetype = filePath.suffix.lower()                  # get the file suffix
        # passing file suffix to folder categorize function
        directory = pickDirectory(filetype)
        # update file path based on file current location
        directoryPath = Path(directory)
        if directoryPath.is_dir != True:                    # create new directory if file category not exist
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))   # move the file


organizeDirectory()
