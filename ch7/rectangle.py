class rectangle:


    


    def set_dimensions(self, hieght,width):
        self.hieght = hieght
        self.width = width
    
    def area(self):
        return self.hieght * self.width
    
    def perimeter(self):
        return 2*(self.hieght + self.width)


#creating obj
rectangle1 =rectangle()
rectangle1.set_dimensions(4,5)
print("the hieght and width are:", rectangle1.hieght, rectangle1.width)
print("the area is:", rectangle1.area())
print("the peri is:", rectangle1.perimeter())