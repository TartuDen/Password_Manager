

class ToSave():
    def __init__(self, data_to_be_added = None) -> None:
        self.to_add = data_to_be_added
        if type(self.to_add) == type(""):
            if "\n" not in self.to_add:
                self.to_add+="\n"
        self.read_data()


    def read_data(self):
        with open(".\\data.txt", "r") as data:
            return(data.read())
    
    def add_data(self):
        with open(".\\data.txt", "a") as data:
            data.write(self.to_add)
            print("next data is successfully added: ", self.to_add)
    
    def delete_all(self):
        with open(".\\data.txt","w") as data:
            data.write("")