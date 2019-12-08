#面向对象, 类class最基本的作用：封装代码
from Jun5 import Human

class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        #Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        print("do_homework")
        super(Student, self).do_homework()



student = Student('长江示范学院','lixue',12)
print(student.get_name())
print(student.do_homework())


