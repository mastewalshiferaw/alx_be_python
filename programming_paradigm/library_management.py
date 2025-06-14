class Book:
  def __init__(self, title, author, _is_checked_out):
    self.title = title
    self.author = author
    self._is_checked_out = False

def check_out(self):
        
        self._is_checked_out = True

    def return_book(self):
        
        self._is_checked_out = False

    def list_available_books(self):
     
    return not self._is_checked_o

class Library:
  def __init__(self):
      self._books = []
  def add_book(self, book):
      self._books.append(book)
  