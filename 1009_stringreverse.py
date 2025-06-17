class StringReverser:
    def __init__(self,text):
        self.text = text
    def reverse(self):
        return self.text [::-1]
    
if __name__ == "__main__":
    s = input("Enter a string to reverse: ")
    reverser = StringReverser(s)
    print("Reversed string: ",reverser.reverse())