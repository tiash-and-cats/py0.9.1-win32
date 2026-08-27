import zipfile
import os

with zipfile.ZipFile("release.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    def addfile(n, a):
        zipf.write(n, a)
        print("+", a)
    
    addfile("src/python.exe", "bin/python.exe")
    addfile("LICENSE.txt", "LICENSE")
    
    # add stdlib
    parent_dir = os.path.dirname("lib")
    for root, dirs, files in os.walk("lib"):
        for file in files:
            file_path = os.path.join(root, file)
            archive_name = os.path.relpath(file_path, parent_dir)
            addfile(file_path, archive_name)