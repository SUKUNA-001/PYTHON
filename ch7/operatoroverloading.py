class complexnumber:

    def __init__(self, real, img):
        self.real = real
        self.img = img


    def __add__(self, other):
        return complexnumber(self.real+other.real, self.img + other.img)


c1 = complexnumber(1,2)        
c2 = complexnumber(3,4)
c3 = c1 + c2
print(c3.real, "+ i", c3.img)