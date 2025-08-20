EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

remaining_bake_time = 0
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time in minutes.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    print(remaining_bake_time)
    return remaining_bake_time

bake_time_remaining(10)

def preparation_time_in_minutes(number_of_layers):
    
    
    """
    Calculate the preparation time based on number of layers.

    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - total preparation time in minutes.
    """
    assumed = 2

    PREPARATION_TIME = number_of_layers * assumed
    print(PREPARATION_TIME)
    return PREPARATION_TIME

preparation_time_in_minutes(2)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed time (prep + bake so far).

    :param number_of_layers: int - number of layers of the lasagna.
    :param elapsed_bake_time: int - minutes the lasagna has baked.
    :return: int - total elapsed time in minutes.
    """
    elapsed = number_of_layers * 2
    elapsed2 = elapsed + elapsed_bake_time
    print(elapsed2)
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
elapsed_time_in_minutes(2, 7)

