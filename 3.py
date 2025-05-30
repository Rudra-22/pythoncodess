class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def displ(self):
        print(f"{self.name} having email.id {self.email}")
class Instructor(User):
    def __init__(self, name, email,subject_expertise):
        super().__init__(name, email,subject_expertise)
        self.subject_expertise = subject_expertise
    def uplod_content(self):
        print(f"NAME {self.name} is delevering the content {self.subject_expertise}")
class CourseCreator(Instructor):
    def __init__(self, name, email, subject_expertise):
        super().__init__(name, email, subject_expertise)
        self.cource = []
    def cource_crte(self,cource,module):
        self.cource = cource
        self.module = module
        print(f"{self.cource}.append has been created by {self.name}")
    def uplod_content(self):
        print(f"{self.name} is cource creator with cource {self.subject_expertise}")
abc =Instructor("RAJ","amn221@gmail.com","C++")
abc.displ()
abc.uplod_content()
creatr=CourseCreator("AMC","amc221@gmail.com","C")
creatr.displ()
creatr.uplod_content()
creatr.cource_crte("C++ BASICS", "Module 1.BASICS","Module 1.OOp")

        
