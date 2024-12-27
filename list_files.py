import os

folders = input("enter folder names with spaces in between. Pls enter the full path : ").split()

for folder in folders:
    counter = 1
    try:
        files = os.listdir(folder)
        print(" ")
        print(" ")
        print(f"Files exists under {folder} are as follows : ")
        print(" ")
    except FileNotFoundError:
        print(f"pls enter a valid folder with the actual path. Folder  {folder} does not exits")
        break

    for file in files:
        print(f"{counter}. {file}")
        counter = counter + 1