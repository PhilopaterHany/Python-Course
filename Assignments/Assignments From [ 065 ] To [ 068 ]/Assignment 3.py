file = open(
    r"P:\Python Course\Assignments\Assignments From [ 065 ] To [ 068 ]\Text Files\txt1.txt", "r")

data = file.read()
lines_count = data.count("\n") + 1
words_count = len(data.split())
chars_count = len(data)  # Including Spaces
l_count = data.count("l")

print(f"Number Of Lines Is => {lines_count}")
print(f"Number Of Words Is => {words_count}")
print(f"Number Of Chars Is => {chars_count}")
print(f"Number Of \"l\" Is => {l_count}")

file.close()
