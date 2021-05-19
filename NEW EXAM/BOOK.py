class book:
    def setvalues(self,Library_name,book_name,author,pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
        print("library name:",self.Library_name)
        print("book name:",self.book_name)
        print("author:",self.author)
        print("pages:",self.pages)
b1=book()
b1.setvalues("public library","as you like it","william shakespeare",200)