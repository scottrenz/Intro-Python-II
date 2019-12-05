from room import Room
from player import Player

# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
# print out some text 
print('___________\n'*10) 
  
# sleep for 2 seconds after printing output 
sleep(2) 
  
# now call function we defined above 
clear() 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].n_ton = 'foyer'
room['foyer'].s_ton = 'outside'
room['foyer'].n_ton = 'overlook'
room['foyer'].e_ton = 'narrow'
room['overlook'].s_ton = 'foyer'
room['narrow'].w_ton = 'foyer'
room['narrow'].n_ton = 'treasure'
room['treasure'].s_ton = 'narrow'

room['outside'].items = " rock stick "
room['foyer'].items = " photo painting "
room['overlook'].items = " plant "
room['treasure'].items = " gold diamond ruby emerald "

#
# Main
#
def take(item):
    if " "+item+" " in room[player1.room].items: 
        room[player1.room].removeitem(item)
        player1.additem(item)
    else:
        print(item + " not there")
    return item
def drop(item):
    if " "+item+" " in player1.items: 
        room[player1.room].additem(item)
        player1.removeitem(item)
    else:
        print("You don't have "+item)
    return item
def com(first):
    if len(first) == 0:
        first = 'x'
    com = first.split()
    first = com[0]
    if len(com) > 1:
        second = com[1]
        if first == 'drop':
            drop(second)
        elif first == 'take' or first == 'get':
            take(second)
        else:
            print("bad input")
    elif first == 'n':
         try:
             x=room[player1.room].n_to
             player1.room = room[player1.room].n_ton
             print(f'new room is: {player1.room}')
         except:
             print("You can't go that way")
    elif first == 'e':
         try:
             x=room[player1.room].e_to
             player1.room = room[player1.room].e_ton
             print(f'new room is: {player1.room}')
         except:
             print("You can't go that way")
    elif first == 's':
         try:
             x=room[player1.room].s_to
             player1.room = room[player1.room].s_ton
             print(f'new room is: {player1.room}')
         except:
             print("You can't go that way")
    elif first == 'w':
         try:
             x=room[player1.room].w_to
             player1.room = room[player1.room].w_ton
             print(f'new room is: {player1.room}')
         except:
             print("You can't go that way")
    elif first == 'q':
          exit()
    else:
          print("\nPlease use one of direction commands: n e w s")
          print("Or one of the commands: take get drop")
          print("followed by an available item to take or drop")
          print("Or to quit use: q")
    return first 
# Make a new player object that is currently in the 'outside' room.
nameask=input("What's your name? ")
player1=Player(Player.getname(Player,nameask),'outside')
com('x')
print(f'\nYou are at {room[player1.room].name}\n')
print(room[player1.room].name," now has: ",room[player1.room].items)
print(player1.name," now has: ",player1.items,'\n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    resp = input("Enter a command: ")
    clear()
    com(resp)
    print('\n',room[player1.room].name," now has: ",room[player1.room].items)
    print(player1.name," now has: ",player1.items)

