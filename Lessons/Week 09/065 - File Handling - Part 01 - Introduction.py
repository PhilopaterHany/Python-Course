# -----------------------------------------------------------------------------------------
# ------------------------------------- File Handling -------------------------------------
# -----------------------------------------------------------------------------------------
# "a" Append => Opens File For Appending Values, Creates File If File Does Not Exist
# "r" Read   => [Default Value] Opens File For Read, Gives Error If The File Does Not Exist
# "w" Write  => Opens A File For Writing, Creates The File If Does Not Exist
# "x" Create => Creates A File, Gives Error If The File Exists
# -----------------------------------------------------------------------------------------

import os

# Main Current Working Directory
print(os.getcwd())

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open("D:\Python\Files\osama.txt")
