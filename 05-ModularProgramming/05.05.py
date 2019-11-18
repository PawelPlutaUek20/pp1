import statistics
wynagrodzenia=[21600, 4350, 3920, 5590, 3250, 4010]
srednia=statistics.mean(wynagrodzenia)
mediana=statistics.median(wynagrodzenia)
odchylenie=f'%.2f'%statistics.stdev(wynagrodzenia)

print(srednia)
print(mediana)
print(odchylenie)