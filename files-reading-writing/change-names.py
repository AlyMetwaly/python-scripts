import os
from pathlib import Path


def change_name():
    for item in os.scandir():
        fileName = item.name
        newName = fileName.lower().replace(" ", "-").replace("_", "-")
        os.rename(fileName, newName)


change_name()
