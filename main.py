import time


def int_input(text="Enter integer: "):
    while True:
        print(text, end="")
        value = input()
        if value.isdecimal():
            return int(value)
        else:
            print("Wrong input")


def counter():
    max_value = int_input("Enter number to count to: ")

    for i in range(0, max_value):
        print(i)
        time.sleep(1)


def timer():
    remaining_seconds = int_input("Enter how many seconds to wait: ")

    while remaining_seconds != 0:
        print(remaining_seconds, "s", sep="")
        remaining_seconds -= 1
        time.sleep(1)

    print("It's ended")


def clock():
    print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))


def get_time():
    time_result = []
    hours = int_input("Enter a hour: ")
    minute = int_input("Enter a minute: ")
    return [hours, minute]


def alarm():
    alarm_time = get_time()
    time_now = time.localtime()

    get_seconds = (alarm_time[0] - time_now.tm_hour) * 360
    get_seconds += (alarm_time[1] - time_now.tm_min) * 60
    get_seconds -= time_now.tm_sec

    if get_seconds <= 0:
        print("Wrong time")
        return

    print("alarm start now.", get_seconds, "seconds to wait")
    time.sleep(get_seconds)
    print("ring ring, it's the alarm")


input_program = {"c": counter, "t": timer, "C": clock, "a": alarm}
program_names = {"c": "counter", "t": "timer",  "C": "clock", "a": "alarm"}
user_inputs = ["c", "t", "C", "a", "q"]


def list_input():
    while True:
        print("choose: ", end="")
        choice = input()
        if choice in user_inputs:
            return choice
        else:
            print("Wrong choice")


def main():
    print("Welcome to Clock program")

    while True:
        print("function list: ")

        for element in program_names:
            print("   '" + element + "' for", program_names[element])
        print("   'q' to quit")

        choice = list_input()

        if choice != "q":
            input_program[choice]()
        else:
            break


main()
