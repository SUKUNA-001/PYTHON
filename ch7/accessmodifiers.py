#public modifiers
class ABC :
    def __init__(self):
        self.__private_attribute = 10 #ths is private attribute

        def __private_function(): #this is a private function
            pass


#protected modifier
class ABC :
    def __init__(self):
        self._protected_attribute = 10 #this is a protected attribute

    def __private_function(): #this is a procted function
        pass    