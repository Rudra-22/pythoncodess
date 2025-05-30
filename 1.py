class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
    def display_info(self):
        print(f"name:{self.name},member_id:{self.member_id}")
class StudentMember(Member):
    def __init__(self,name,member_id):
        super().__init__(name,member_id)
        self.borrow_book = []
    
    def add_book(self,book):
        self.borrow_book.append(book)
        print(f"{book}has borrowedby {self.name}")
    def return_book(self,book):
        if book in self.borrow_book:
            self.borrow_book.remove(book)
            print(f"{book} has been been returned by {self.name}")
        else:
            print(f"{book} has not been returned yet by {self.name}")
    def displ_borrow(self):
        print(f"{self.name} status")
        if self.borrow_book:
            print(f"{self.borrow_book} book borrowed  ")
            print("TOTAL BOOK BOROOWED {self.borrow_book}")
        else:
            print(f"NO BOOK BOROWED")
stud=StudentMember("RAJ","I23")
stud.display_info()
stud.add_book("PYTHON")
stud.add_book("JAVA")
stud.displ_borrow()
stud.return_book("JAVA")
stud.displ_borrow()
