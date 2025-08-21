def convert(n):
    Sound = ""
    if(n % 3 == 0):
        Sound += "Pling"
    if(n % 5 == 0):
        Sound += "Plang"
    if(n % 7 == 0):
        Sound += "Plong"
    if(n % 3) and (n % 5) and (n % 7) != 0: Sound = str(n)

    return Sound