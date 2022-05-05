import time


def counter():
    pass


def timer():
    pass


def clock():
    pass


def alarm():
    pass


input_program = {"c": counter, "t": timer, "C": clock, "a": alarm}
program_names = {"c": "counter", "t": "timer",  "C": "clock", "a": "alarm"}
user_inputs = ["c", "t", "C", "a", "q"]


def user_input():
    return "t"


def main():
    print("Welcome to Clock program")

    while True:
        print("function list: ")

        for element in program_names:
            print("   '", element, "' for ", program_names[element])
        print("   ' q ' to quit")

        choice = user_input()

        if choice != "q":
            input_program[choice]()
            break
        else:
            break


main()
