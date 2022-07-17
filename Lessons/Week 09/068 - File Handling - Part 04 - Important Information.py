# --------------------------------------------
# -- File Handling => Important Information --
# --------------------------------------------

import os

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)

myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell())

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("D:\Python\Files\osama.txt")
