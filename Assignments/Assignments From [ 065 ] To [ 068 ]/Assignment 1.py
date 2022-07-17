import os

i = 1
while (i <= 50):
    if i == 25:
        file = open(r"P:\Python Course\Assignments\Assignments From [ 065 ] To [ 068 ]\Text Files\special-text.txt", "w")
        file.close()
    else:
        file = open(fr"P:\Python Course\Assignments\Assignments From [ 065 ] To [ 068 ]\Text Files\txt{i}.txt", "w")
        file.write(f"Elzero Web School => {i}\n")
        file.close()
    i += 1

file = open(r"P:\Python Course\Assignments\Assignments From [ 065 ] To [ 068 ]\Assignment 1.py")
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.basename(file.name))
print("There Are", str(len(os.listdir(f"P:\Python Course\Assignments\Assignments From [ 065 ] To [ 068 ]\Text Files"))), "Files In The Directory.")
file.close()
