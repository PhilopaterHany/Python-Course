# --------------------------------------------------------------------------------------
# -------------------- Regular Expressions => Re Module Split & Sub --------------------
# --------------------------------------------------------------------------------------
# split(Pattern, String, MaxSplit) => Returns A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replaces Matches With What You Want
# --------------------------------------------------------------------------------------

import re

string_one = "I Love Python Programming Language"
search_one = re.split(r"\s", string_one, 1)
print(search_one)

print("=" * 50)  # Separator

string_two = "How-To_Write_A_Very-Good-Article"
search_two = re.split(r"-|_", string_two)
print(search_two)

print("=" * 50)  # Separator

# Get Words From URL
for counter, word in enumerate(search_two, 1):
    if len(word) == 1:
        continue
    print(f"Word Number: {counter} => {word.lower()}")

print("=" * 50)  # Separator

my_string = "I Love Python"
print(re.sub(r"\s", "-", my_string, 1))
