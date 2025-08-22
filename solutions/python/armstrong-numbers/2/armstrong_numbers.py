def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]  # list of digits
    power = len(digits)                     # number of digits
    return number == sum(d ** power for d in digits)
    
