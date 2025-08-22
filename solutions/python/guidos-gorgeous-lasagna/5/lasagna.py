EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

remaining_bake_time = 0
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    print(remaining_bake_time)
    return remaining_bake_time

bake_time_remaining(10)

def preparation_time_in_minutes(number_of_layers):
    assumed = 2

    PREPARATION_TIME = number_of_layers * assumed
    print(PREPARATION_TIME)
    return PREPARATION_TIME
    """Form the preparation time in minutes of preparing the lasagna
    :param preparation_time: int * number of layers
    :return: int * number of layers
    

    Keyword arguments:
    number_of_layers -- number of layers of the lasagna
    """


preparation_time_in_minutes(2)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    elapsed = number_of_layers * 2
    elapsed2 = elapsed + elapsed_bake_time
    print(elapsed2)
    return elapsed2
    """Form the elapsed time in minutes of the lasagna cooking procedure.
    :param elapsed_time_in minutes: in * number of layers
    :return: int * number of layers
    

    Keyword arguments:
    number_of_layers -- number of layers of the lasagna
    elapsed_bake_time -- the already elapsed baking time
    """

elapsed_time_in_minutes(2, 7)

