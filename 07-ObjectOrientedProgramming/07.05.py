class Songs():
    def __init__(self, autor, title, album, year):
        self.autor = autor
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f'Wykonawca: {self.autor}\nUtwor: {self.title}\nAlbum: {self.album}\nRok: {self.year} '
s1 = Songs("Dawid Podsiadlo", "Nie ma fal", "Malomiasteczkowy", 2018)
print(s1)