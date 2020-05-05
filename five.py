"""  
    For this problem you will modify a function that creates a password
    the password needs to include features from the input list
    that contains information about the person.
    Passwords need to have 3 random special characters
    contain jumbled strings from the input
    include 2-4 numbers
    be of lenght 18-36 characters
    NOTE: 0 points if when you run the code again, the password is similar.
          Every time you run the code you should get a unique string. 
"""
import random


def passwordGenerator(personal_list):

    outputList = []
    personal_list = [x for x in personal_list if not isinstance(x, int)]

    # Removes integers from list
    listWithNoInts = []
    for i in personal_list:
        if isinstance(i, str):
            listWithNoInts.append(i)
        if isinstance(i, list):
            listWithNoInts.extend(i)

    # Takes items in inner list and add them separately to list
    rand1 = random.randint(2, 4)

    for i in range(rand1):
        outputList.append(str(random.randint(0, 9)))

    # adds random numbers to password creation list
    rand2 = random.choice(listWithNoInts)
    rand3 = random.choice(listWithNoInts)
    rand4 = random.choice(listWithNoInts)
    rand5 = random.choice(listWithNoInts)

    outputList.append(rand2)
    outputList.append(rand3)
    outputList.append(rand4)
    outputList.append(rand5)

    # randomly selects 4 items from list and adds them to password creation list
    specials = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
                '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    rand6 = random.choice(specials)
    rand7 = random.choice(specials)
    rand8 = random.choice(specials)

    outputList.append(rand6)
    outputList.append(rand7)
    outputList.append(rand8)

    holder = 0
    for i in outputList:
        char_list = list(i)
        random.shuffle(char_list)
        finalStr = ''.join(char_list)
        outputList[holder] = finalStr
        holder = holder + 1

    # shuffles the strings in the list
    random.shuffle(outputList)

    # shuffles the order of items
    password = ''.join(outputList)

    return password


if __name__ == "__main__":
    mylist = [12, "BOB", -2, "Amy", ["David", "Jona", "Timmothy"], "Burt"]
    print(passwordGenerator(mylist))
