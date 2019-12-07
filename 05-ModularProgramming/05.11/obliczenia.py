from dane import pobierzDane
import statistics
dane = pobierzDane()
def srednia():
    srednia=statistics.mean(dane)
    return srednia

def mediana():
    mediana=statistics.median(dane)
    return mediana

def minimum():
    minimum=min(dane)
    return minimum

def maksimum():
    maksimum=max(dane)
    return maksimum