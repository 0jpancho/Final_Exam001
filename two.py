""" Playing with Functions 
    For this second problem use only the function calls available and the starting variable to make ALL of the print statements correct.
    Note you may only modify the characters to the left of result = ...
    You may not modify any other lines of code, you may not use symbols like '+', '*', '//', '/', or '-'
"""


def performCalculations(value):



    result = value
    return result


def f1(v1, v2):
    return v1 // v2


def f2(v3, v4):
    return v4 + v3


def f3(v1, v2):
    return v2 - v1


def f4(v):
    return v * v


def f5(v1, v2):
    return v1 / v2


def tester(input, output):
    actual_result = performCalculations(input)
    expected_result = output
    print_text = "In: " + str(input) + " | "
    if expected_result == actual_result:
        print_text += "Correct: " + str(expected_result) + " == " + str(actual_result)
    else:
        print_text += "Incorrect: " + str(expected_result) + " != " + str(actual_result)
    return print_text


if __name__ == "__main__":
    print(tester(350, 696))
    print(tester(37, 70))
    print(tester(-40, -85))
    print(tester(-2, -9))
    print(tester(15, 26))
