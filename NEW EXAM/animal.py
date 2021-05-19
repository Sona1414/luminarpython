class animal:
    def __init__(self,type):
        self.type=type
        print("TYPE:",self.type)
class dog(animal):
    def __init__(self,name,breed,type):
        self.name=name
        self.breed=breed
        super().__init__(type)
        print("name:",self.name)
        print("breed:",self.breed)
d1=dog("pluto","lab","carnivores")
