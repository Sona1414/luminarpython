class book:
    def setvalues(self,name,author):
        self.name=name
        self.author=author
        print("name:",self.name)
        print("author:",self.author)
class seller(book):
    def setvalues(self,storename,sellername):
        self.storename=storename
        self.sellername=sellername
        print("store name:",self.storename)
        print("seller name:",self.sellername)
s1=seller()
s1.setvalues("books","rajiv")