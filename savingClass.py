import json

class ToSave():
    def __init__(self, data_to_be_added = None) -> None:
        self.to_add = data_to_be_added
        if type(self.to_add) == type(""):
            if "\n" not in self.to_add:
                self.to_add+="\n"
        # self.read_data()


    def read_data(self):
        with open(".\\data.json", "r") as data_file:
            return(json.load(data_file))

    
    def add_data(self):
        try:
            with open(".\\data.json", "r") as data_file:
                original_data = json.load(data_file)
                original_data.update(self.to_add)
            with open(".\\data.json", "w") as data_file:
                json.dump(original_data, data_file, indent=4)

        except FileNotFoundError:
            with open(".\\data.json", "w") as data_file:
                original_data = json.dump(self.to_add,data_file, indent=4)
            
        
