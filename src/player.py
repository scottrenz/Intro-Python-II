# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = ' ball bat '
    def getname(self, name_in):
        self.name = name_in
        print(f'\nHello {name_in}')
        return name_in
    def additem(self, item_in):
        self.items += " " + item_in + " "
        self.items = self.items.replace("  "," ",99)
        print(f'\n added {item_in} to {self.name}')
        return item_in    
    def removeitem(self, item_out):
        self.items = self.items.replace(" " + item_out + " "," ",9)
        self.items = self.items.replace("  "," ",99)
        print(f'\n removed {item_out} from {self.name}')
        return item_out    
        
