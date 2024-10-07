class school:
    def __init__(self,branch,teacher,department,avaliable):
        self.branch = branch
        self.teacher= teacher
        self.department=department
        self.avaliable=avaliable
   

    def show_info(self):
        print("-"*45)
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nAvaliable Student: {}".format(self.branch,self.teacher,self.department,self.avaliable))
        print("-"*45)

    
    def teacher_name(self):
        print("Teacher name: ",self.teacher)





first_class =school("12-a","Emre","SE","25")
first_class.show_info()

second_class =school("12-B","Ahmet","CE","56")
second_class.show_info()
second_class.teacher_name()