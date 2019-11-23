import statistics
XYZ=[21600,4350,3920,5590,3250,4010]
aryt = statistics.mean(XYZ)
medi = statistics.median(XYZ)
stdev = statistics.stdev(XYZ)

print(f'Średnia artymetyczna = {aryt}\n')
print(f'Mediana = {medi}\n')
print(f'Odchylenie standardowe = {stdev}')
