class Student():
    album_nr = 100000
    
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.album = Student.album_nr
        Student.album_nr += 1
    
    def __str__(self):
        return f'{self.name} {self.surname.upper()} ({Student.album_nr}), {self.course}, UEK Krakow'

s1 = Student("Wacław", "Potocki", "Informatyka stosowana")
s2 = Student("Pawel", "Pluta", "Informatyka stosowana")
print(s1)
print(s2)