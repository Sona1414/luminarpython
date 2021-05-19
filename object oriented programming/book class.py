class Book:
    def __init__(self,author,bookname,pages):
        self.author=author
        self.bookname=bookname
        self.pages=pages
    def print(self):
        print("AUTHOR:",self.author)
        print("BOOK NAME:",self.bookname)
        print("NO OF PAGES:",self.pages)
    def __str__(self):
        return self.bookname+self.author+str(self.pages)
b1=Book("WILLIAM SHAKESPEARE","AS YOU LIKE IS",100)
b1.print()
print(b1)#here we get an address as output to get the common name to the object as output
#here str function return only a single value so we have to concatenate the other values if needed
#it only returns a string value