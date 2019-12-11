class Student():
    album_nr = 100000
    
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.album = Student.album_nr
        Student.album_nr += 1
    
    def __str__(self):
        return f'{self.name} {self.surname.upper()} ({self.album}), {self.course}, UEK Krakow'

s1 = Student("Pawel", "Pluta", "Informatyka stosowana")
s2 = Student("Wacław", "Potocki", "Informatyka stosowana")
s3 = Student("Ronald", "Donald", "Gastronomia")
print(f'{s1}\n{s2}\n{s3}')
