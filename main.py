import glob
import os
import shutil
from threading import Thread

extension = ['png', 'jpg', 'heic', 'jpeg', 'mp4']
root_dir = [chr(x) + ":\\" for x in range(65,91) if os.path.exists(chr(x) + ":")]
exclusions = [
    "AppData", 'Midas Gen', 'midas Design+', 'Lumion', 'DroidCam', 'Program Files',
    'Program Files (x86)', 'ProgramData', 'Autodesk', 'Windows', 'DRIVER', 'STAAD.Pro',
    'SketchUp 2019', 'obs-studio', 'Steam'
    ]

def copy(source, destination):
    try:
        shutil.copy2(source, destination)
    except shutil.SameFileError:
        shutil.copy2(source, destination + "SameName\\")

for directory in root_dir:
    if os.path.isdir(directory):
        if os.getcwd().split(':')[0] != directory.split(':')[0].lower():
            for ext in extension:
                image_list = []
                for filename in glob.iglob(directory + '**/*.' + ext, recursive=True):
                    if not any(item in exclusions for item in filename.split("\\")):
                        if filename not in image_list:
                            image_list.append(filename)

                for image in image_list:
                    Thread(target=copy, args=(image, '.\\Transfered_images\\')).start()
