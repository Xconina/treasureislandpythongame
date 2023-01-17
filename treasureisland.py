#This is a python game

print("Welcome to Treasure Island.\n Your mission is to find the treasure. Enter 'start' to begin")
starting = input()
if starting == "start":
    print("The game has begun")
    print("You are at a crossroads. Do you go left or right?")
    leftorright = input()

    if leftorright == "left":
        print("You died.")
    else:
        print("You make your way to the beach. You find a seashell. Type 'a' to pick it up, or 'b' to leave it.")
    shell = input()
    if shell == "a":
        print("The shell contained a vicious crab that bites your hand off. You must retreat.")
    else:
        print("You leave the shell and continue on. You find a map on the sand. It says treasure is west.\n Type 'a' to take the longer route, type 'b' to take the shorter route.")
    route = input()
    if route == "b":
        print("You head towards the ocean but you don't know how to swim. You drown.")
    else:
        print("You venture towards the trees.")



else:
    print("game over")

