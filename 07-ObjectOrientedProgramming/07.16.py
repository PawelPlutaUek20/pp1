class Student:
    def __init__(self, name, surname, album_nr):
        self.name = name
        self.surname = surname
        self.album_nr = album_nr
        
    def __str__(self):
        return f"{self.name} {self.surname} {self.album_nr}"
    
    def __eq__(self, other):
            return self.album_nr == other.album_nr

    def __lt__(self, other):
            return self.album_nr < other.album_nr
        
    def __repr__(self):
        return repr((self.name, self.surname, self.album_nr))
           
s1 = Student("Anna", "Tomaszewska", 141820)
s2 = Student("Wojciech", "Zbych", 201003)
s3 = Student("Maja", "Kowalska", 153202)
s4 = Student("Marek", "Migiel", 138600)

Student.__lt__ = lambda self, other: self.album_nr < other.album_nr
student_objects = [s1,s2,s3,s4]
print(*sorted(student_objects),sep="\n")



