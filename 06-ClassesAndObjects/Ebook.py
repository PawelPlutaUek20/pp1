class ebook():   
    def __init__(self, title, autor, total_pages, current_page):
        self.title = title
        self.autor = autor
        self.total_pages = total_pages 
        self.current_page = current_page
        self.is_opened = False
        
    def open(self):
        self.is_opened = True
    def close(self):
        self.is_opened = False
    def next_page(self):
        if self.current_page in range(304) and self.is_opened:
            self.current_page += 1
        elif not self.is_opened:
            print("The book is closed")
    def previous_page(self):
        if self.current_page in range(2,305) and self.is_opened:
            self.current_page -= 1
        elif not self.is_opened:
            print("The book is closed")
    def show_status(self):
        if self.is_opened:
            print(f"Title: {self.title}\nAutor: {self.autor}\nTotal pages: {self.total_pages}\nCurrent page: {self.current_page}\n")