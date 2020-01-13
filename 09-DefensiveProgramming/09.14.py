def pole_prostokata(a,b):
    assert (type(a) == float or type(a) == int) and a > 0
    assert (type(b) == float or type(b) == int) and b > 0
    return a*b

print(pole_prostokata(3,4))
print(pole_prostokata(3.1,4.0))
print(pole_prostokata(3.1,"4"))
print(pole_prostokata(3,-2))