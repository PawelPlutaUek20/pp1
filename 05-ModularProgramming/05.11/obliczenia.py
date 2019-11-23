from dane import pobierzDane
import statistics
def srednia():
    srednia=statistics.mean(pobierzDane())
    return srednia

def mediana():
    mediana=statistics.median(pobierzDane())
    return mediana

def minimum():
    minimum=min(pobierzDane())
    return minimum

def maksimum():
    maksimum=max(pobierzDane())
    return maksimum