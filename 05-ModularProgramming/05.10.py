from QuadraticEquation import *
print('Równanie kwadratowe postaci:',end=' ')
if b>0:
    b=f'+{b}'
elif b==0:
    b=''
if c>0:
    c=f'+{c}'
elif c==0:
    c=''   
if a==1:
    print(f'x²{b}x{c}=0')
else:
    print(f'{a}x²{b}x{c}=0')
if len(pierwiastki)==2:
    print(f'Pierwiastki równania: x₁={x1}, x₂={x2}')
elif len(pierwiastki)==1:
    print(f'Pierwiastek równania: x₀={x0}')
elif len(pierwiatki)==0:
    print(f'Równanie nie ma pierwiastków')