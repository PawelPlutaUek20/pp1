student = 'Mateusz'
assert type(student) == str
stypendium = 950
assert (type(stypendium) == int or type(stypendium) == float) and stypendium >=0
wydatki = 920
assert wydatki < stypendium and wydatki >=0 and (type(wydatki) == int or type(wydatki) == float)
print('Student: {}'.format(student.upper()))
print('stypendium: {} zł'.format(stypendium))
print('Wydatki: {} zł'.format(wydatki))
print('Oszczędności: {} zł'.format(stypendium-wydatki))