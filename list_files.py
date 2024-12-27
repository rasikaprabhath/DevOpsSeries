import os

folders = input("enter folder names with spaces in between. Pls enter the full path : ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"pls enter a valid folder with the actual path. Folder  {folder} does not exits")
        break
    print(files)

    for file in files:
        print(file)