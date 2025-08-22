def square(number):
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    
    else:
        return 2 ** (number - 1)


def total():
    return (2 ** 64) - 1

# edited code to be more in the form of the PEP-0008