#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 12, 2021
# Determines the largest number out of three


def main():
    # Input
    user_input1 = (input("Enter your first number: "))
    user_input2 = (input("Enter your second number: "))
    user_input3 = (input("Enter your third number: "))

    if user_input1.isdigit():
        if user_input2.isdigit():
            if user_input3.isdigit():
                number1 = int(user_input1)
                number2 = int(user_input2)
                number3 = int(user_input3)
                if (number1 > number2 and number1 > number3):
                    print("The greatest number is: {}".format(number1))
                elif (number2 > number1 and number2 > number3):
                    print("The greatest number is: {}".format(number2))
                else:
                    print("The greatest number is: {}".format(number3))
            else:
                print("{} is not an integer".format(user_input3))
        else:
            print("{} is not an integer".format(user_input2))
    else:
        print("{} is not an integer".format(user_input1))


def done():
    print("Done.")


if __name__ == "__main__":
    main()
    done()
