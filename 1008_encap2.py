class Encapnumber():
    def __init__(self,number):
        self.__number = number
    def get_number(self):
        return self.__number
    def set_number(self,new_number):
        self.__number = new_number
    def show_number(self):
        print(f"Encapsulated Number: {self.__number}")
        
if __name__ == "__main__":
    encap = Encapnumber(42)
    encap.show_number()
    encap.__number = 55
    encap.show_number()
    encap.set_number(3.14)
    encap.show_number()