"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Returning True if the criteria for being critically balanced is met:
    
    Keyword arguments:
    temperature -- Temperature measured in kelvin
    neutrons_emitted -- The neutrons emitted
    """
    product = temperature * neutrons_emitted
    return (temperature < 800) and (neutrons_emitted > 500) and (product < 500000)  


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Determine the Power output range:

    Keyword arguments:
    voltage -- The voltage of the reactor
    current -- The current watt (?)
    theoretical_max_power -- The theoretical maximunm power of the reactor
    """
    generated_power = voltage * current
    percentage = (generated_power / theoretical_max_power) * 100

    if percentage >= 80:
        return "green"
    
    if 60 <= percentage < 80:
        return "orange"
        
    if 30 <= percentage < 60:
        return "red"
    
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Returning for the following criterias (described in the lower part of this docstring):

    Keyword arguments:
    temperature -- measured in kelvin
    neutrons_produced_per_second -- value of neutrons produced per second
    threshold -- the 'safe value' of what is considered safe reactor output
    
    'LOW': if calc < 90% of threshold
    'NORMAL': if calc is within 10% of the threshold
    'DANGER': if calc is not in the above
    
    """
    calc = temperature * neutrons_produced_per_second
    
    if calc < 0.9 * threshold:
        return "LOW"
    
    if 0.9 * threshold <= calc <= 1.1 * threshold:
        return "NORMAL"
    
    return "DANGER"
    
