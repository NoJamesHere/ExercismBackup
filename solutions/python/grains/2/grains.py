def square(number):
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    if(not number):
        raise ValueError("No square is given")
    return 2 ** (number - 1)


def total():
    return (2 ** 64) - 1