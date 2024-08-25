class animal:
    def speaks(self):#abstract method which will be overwritten
        pass

class dog(animal):
    def speak(self):
        print("bark")


class cat(animal):
    def speak(self):
        print("meow")

class cow(animal):
    def speak(self):
        print("moo")        


dog = dog()            
cat = cat()
cow = cow()

dog.speak()
cat.speak()
cow.speak()