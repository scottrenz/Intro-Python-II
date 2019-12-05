
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = ''
    def additem(self, item_in):
        self.items += " " + item_in
        print(f'\n added {item_in} to {self.name}')
        return item_in    
    def removeitem(self, item_out):
        self.items = self.items.replace(" " + item_out + " "," ",9)
        self.items = self.items.replace("  "," ",99)
        print(f'\n removed {item_out} from {self.name}')
        return item_out    
    def __str__(self):
        return f'\n\tThis is room "{self.name}"". "{self}"".'
