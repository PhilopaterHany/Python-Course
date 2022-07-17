# ---------------------------------------------------------------------------------------------
# --------------------- Regular Expressions => Re Module Search & FindAll ---------------------
# ---------------------------------------------------------------------------------------------
# search()  => Searches A String For A Match And Returns The First Match Only
# findall() => Returns A List Of All Matches And Returns An Empty List if No Matches Were Found
# ---------------------------------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ---------------------------------------------------------------------------------------------

import re

my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(my_search)
print(my_search.span())
print(my_search.string)
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")
if is_email:
    print("This is A Valid Email")
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())
else:
    print("This is Not A Valid Email")

email_input = input("Write Your Email: ")
search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)
empty_list = []
if search != []:
    empty_list.append(search)
    print("Email Added")
else:
    print("Invalid Email")

for email in empty_list:
    print(email)
