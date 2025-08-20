def is_armstrong_number(number):
    n = str(number)
    power = len(n)                     # number of digits
    return number == sum(int(d) ** power for d in n)

# removed unnecessary logic