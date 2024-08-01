def read(message=""):
    return input(message)


def readint(message="", messageerror="Invalid input. Please enter an integer."):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(messageerror)


def readfloat(message="", messageerror="Invalid input. Please enter an float."):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(messageerror)
