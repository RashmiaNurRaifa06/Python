class details:
    __password = "Code123"
    name = "Jon"
    
    def __getUsername(self):
        print("user779")
    def getData(self):
        print("Password: ", details.__password)
        
a = details()

a.getData()        