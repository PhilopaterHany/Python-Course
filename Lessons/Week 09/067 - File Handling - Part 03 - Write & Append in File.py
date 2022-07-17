# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Osama\n", "Mohamed\n", "Philopater\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.write("Elzero")
