"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    product = temperature * neutrons_emitted
    return (temperature < 800) and (neutrons_emitted > 500) and (product < 500000)
    


def reactor_efficiency(voltage, current, theoretical_max_power):
    generatedPower = voltage * current
    percentage = (generatedPower / theoretical_max_power) * 100

    if(percentage >= 80):
        return "green"
    elif(60 <= percentage < 80):
        return "orange"
    elif(30 <= percentage < 60):
        return "red"
    else: return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    calc = temperature * neutrons_produced_per_second
    if(calc < 0.9 * threshold):
        return "LOW"
    elif(0.9 * threshold <= calc <= 1.1 * threshold):
        return "NORMAL"
    else: return "DANGER"
    
