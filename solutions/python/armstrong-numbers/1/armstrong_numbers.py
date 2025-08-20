def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]  # list of digits
    power = len(digits)                     # number of digits
    total = sum(d ** power for d in digits)
    if(total == number):
        return True
    else:
        return False
