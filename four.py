"""
    In this problem you will open a file (four.txt), you will read some information from the file
    then you will right a output of that information to a new file solution4.txt
    1) On every line of the file input there is a character that is uppper or lower when
    the other characters are the opposite
    Concatenate all of these characters to build a message.
    2) Sum all of the numbers on the first 10 lines, call this final number J
       Split the 11th line on the most frequent character
       the word at the Jth position can be called the Fword
       Return the number of times that the Fword appears in the file case insensitive.
    3) In solution4.txt output on the first line the message, the next line the frequency
    Example solution4.txt:
    "Hidden Message"
    34

"""


def questionOne():
    inputF = open("four.txt", 'r')
    outputF = open("solution4.txt", 'w')

    for line in inputF:
        outputString = ""
        for i in line:
            if i.isupper():
                outputString = outputString + i
            else:
                pass
        outputF.write(outputString)

    inputF.close()
    outputF.close()


def questionTwo():
    inputF = open("four.txt", 'r')

    numbers = '0123456789'

    countTracker = 0

    finalNum3 = 0

    for count in range(10):
        print("Count: " + str(count))
        countTracker = count
        for line in inputF:
            for i in line:
                if i in numbers:
                    print(i)
                    finalNum3 = finalNum3 + int(i)
    print(finalNum3)

    for i in inputF:
        countTracker = countTracker + 1
        print("Count Tracker: " + countTracker)
        if int(i) == 9:
            print("works")

    inputF.close()

if __name__ == "__main__":
    questionOne()
    questionTwo()
