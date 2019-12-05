# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def getname(self, name_in):
        self.name = name_in
        print(f'\nHello {name_in}')
        return name_in    
    def __str__(self):
        return f'\nYou are at'
