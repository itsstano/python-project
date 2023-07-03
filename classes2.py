class people:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name,self.age,self.gender)
myobj=people("Darryl",20,"Male")
myobj.display()
myobj=people("Lance",23,"Male")
myobj.display()
myobj=people("Irene",24,"Female")
myobj.display()