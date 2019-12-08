from ebook import ebook
eb = ebook("The Hobbit", "J.R.R. Tolkien", 304, 1)
eb.open()
eb.show_status()
for _ in range(3):
    eb.next_page()
eb.show_status()
eb.close()
eb.next_page()