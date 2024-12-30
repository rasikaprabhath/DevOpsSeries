'''This peice of code demo how files of  given folders of your local machine is listed.
you can specify folder name with the full path seperating by spaces
'''
import os
#take the input from the CLI. seperate folders with the space.
# split() will identify the space and split the string
#folders will store these strings in a list
folders = input("enter folder names with spaces in between. Pls enter the full path : ").split()

#traversing through the list to find folders
for folder in folders:
#counter is used to dispaly the sequence number in front of the file name
    counter = 1
#error handling for FileNotFound Exception
    try:
        files = os.listdir(folder)
        print(" ")
        print(" ")
        print(f"Files exists under {folder} are as follows : ")
        print(" ")
    except FileNotFoundError:
        print(f"pls enter a valid folder with the actual path. Folder  {folder} does not exits")
        break
#printing the files inside the folder
    for file in files:
        print(f"{counter}. {file}")
        counter = counter + 1