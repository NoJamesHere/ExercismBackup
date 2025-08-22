def is_armstrong_number(number):
    power = len(str(number))                     # number of digits
    return number == sum(int(d) ** power for d in str(number))

# removed unnecessary logic