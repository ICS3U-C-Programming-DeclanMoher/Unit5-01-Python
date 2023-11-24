#!/usr/bin/env python3
# created Nov 24th 2023 by Declan Moher
def tempcovert():
    # getting input in celsius
    celsius_covert_str = input("Enter a temperature ")
    try:
        # casting to integer
        celsius_covert_int = int(celsius_covert_str)
    except ValueError:
        # if they can't put it into a integer this will print
        print(f"{celsius_covert_str} is an incorrect input please enter an integer")
    else:
        # calculating input  into fahrenheit
        fahrenheit = (celsius_covert_int * 9 / 5) + 32
        print(
            f"{fahrenheit} degrees fahrenheit is if you put {celsius_covert_str} degrees celsius"
        )


def main():
    # function call
    tempcovert()


if __name__ == "__main__":
    main()
