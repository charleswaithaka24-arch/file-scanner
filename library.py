class library:
  def __init__(self,name):
    self.name=name
    self.books=[]
    self.borrowed=[]

  def add(self,book):
    self.books.append(book.title)

  def remove(self,book):
    if book.title not in self.books:
      print("Book not in library")
    else:
     self.books.remove(book.title)

  def borrow(self,book):
    if book.title not in self.books:
      print("Book not found")
    else:
      self.books.remove(book.title)
      self.borrowed.append(book.title)

  def ret(self,book):
    self.borrowed.remove(book.title)
    self.books.append(book.title)

class book:
  def __init__(self,title,author):
    self.title=title
    self.author=author

heritage=library("Heritage")

book_1=book("The river between","Ngugi wa Thiong'o")
book_2=book("Harry Potter","J.R.R. Rolins")
book_3=book("Genesis","Moses")
book_4=book("Proverbs","Solomon")

heritage.add(book_1)
heritage.add(book_2)
heritage.add(book_3)

heritage.borrow(book_4)