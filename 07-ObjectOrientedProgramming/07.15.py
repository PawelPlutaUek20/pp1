class Book:
    def __init__(self, title, author, language, genre):
        self.title = title
        self.author = author
        self.language = language
        self.genre = genre
class Ebook(Book):
    def __init__(self, title, author, language, genre, file_name):
        Book.__init__(self, title, author, language, genre)
        self.file_name = file_name
    def __str__(self):
        return f'''Title: {self.title}
Author: {self.author}
Language: {self.language}
Genre: {self.genre}
File: {self.file_name}'''
class Tbook(Book):
    def __init__(self, title, author, language, genre, pages):
        Book.__init__(self, title, author, language, genre)
        self.pages = pages
    def __str__(self):
        return f'''Title: {self.title}
Author: {self.author}
Language: {self.language}
Genre: {self.genre}
Pages: {self.pages}'''

t = Tbook("Harry Potter and the Goblet of Fire", "J.K. Rowling", "English", "Fantasy", 734)
e = Ebook("The Lord of the Rings", "	J.R.R. Tolkien", "English", "Fantasy", "LoR.txt")

print(f"{e}\n\n{t}")