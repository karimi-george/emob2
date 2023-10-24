class Students:
    def __init__(self,name,course,gender,age):
        self.name =name
        self.course = course
        self.gender = gender
        self.age = age

    def dispaly(self):
        print("Name: %s \nCourse: %s\nGender: %s\nAge:%d"%(self.name, self.course,self.gender,self.age))
myobj=Students("Erick","computer science","male",28)
myobj2=Students("grace","marketing","female",59)
myobj2.dispaly()
myobj.dispaly()