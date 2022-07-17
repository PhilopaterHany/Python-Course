my_friends = []
max_friends = 4
while max_friends > 0:
    friend = input("Enter Your Friend Name To Be Added: ").strip()
    if friend.isupper():
        print("Sorry, Invalid Name.")
    else:
        friend = friend.capitalize()
        my_friends.append(friend)
        max_friends -= 1
        print(f"Your Friend '{friend}' Added To The List (1st Letter Became Capital).")
        print(f"There are {max_friends} Empty Names Left In The List." if max_friends != 0 else "Sorry, The List Is Full. You Cannot Add More Friends.")
else:
    print("Your Friends: {my_friends}")
