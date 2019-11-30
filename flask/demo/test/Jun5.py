class Human():
    sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('parant init')

    def get_name(self):
        print("the girl is " + self.name)

    def do_homework(self):
        print('parent')