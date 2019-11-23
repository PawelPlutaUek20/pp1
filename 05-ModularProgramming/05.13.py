def backwards():
    x = 'uniwersytet ekonomiczny w KRAKOWIE'
    return x[::-1]
def spaces():
    y = 'uniwersytet ekonomiczny w KRAKOWIE'
    return ' '.join(y)
def capitalized():
    z = 'uniwersytet ekonomiczny w KRAKOWIE'
    import string
    return string.capwords(z)

try:
    x = backwards()
    y = spaces()
    z = capitalized()
    if x == 'EIWOKARK w ynzcimonoke tetysrewinu' and y == 'u n i w e r s y t e t   e k o n o m i c z n y   w   K R A K O W I E' and z == "Uniwersytet Ekonomiczny W Krakowie":
        print('WYKONANO POPRAWNIE')
except:
    pass