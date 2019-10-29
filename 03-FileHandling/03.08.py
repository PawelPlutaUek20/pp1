# wariant 1
file = open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/NoEducation.txt', 'r')
print(file.read())
file.close()

# wariant 2
with open('C:/Users/Paweł/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    print(file.read())