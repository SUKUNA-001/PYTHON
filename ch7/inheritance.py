
class parent:
    def __init__(self):
        self.super_attribute = True
        print("this is parent class")


class child(parent):
    def __init__(self):
        super().__init__()
        print("This is child class")
        print(self.super_attribute)


child = child()