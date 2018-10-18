class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname

    def __str__(self):
      return "{} {}".format(self.firstname,self.lastname)

    def eat(self, food):
        print("{} will eat {}".format(self, food))

class Student(Person):

    def __init__(self, firstname, lastname, school = ""):
        super().__init__(firstname, lastname)   
        self.school = school

    def __str__(self):
        return "{} [{}]".format (super().__str__(),
        self.school) 

if __name__== "__main__":
    
      cyrus = Person("Cyrus", "Requiro")
      print (cyrus)

      cyrus.eat("nothing")

      ugoks = Student("ugoks", "manggo", "ADNU")
      print (ugoks)