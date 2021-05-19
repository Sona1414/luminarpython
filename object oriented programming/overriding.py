#overriding--same method name, same number of parameters in both parent and child class
class Parent:
    def details(self):
        print("sona")
class child(Parent):
    def details(self):
        print("rahul")
ch=child()
ch.details()