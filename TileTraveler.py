def North(place):
    place +=1
    return (place)

def South(place):
    place -=1
    return (place)

def East(place):
    place +=10
    return (place)

def West(place):
    place -=10
    return (place)

place=11
while place != 31:
    if place == 11 or place == 21:
        print("You can travel: (N)orth.")
        direction = (input("Direction: ")).lower()
        if direction == "n":
            place = North(place)
        else:
            print("Not a valid direction!")
    if place == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = (input("Direction: ")).lower()
        if direction == "n":
            place = North(place)
        elif direction == "s":
            place = South(place)
        elif direction == "e":
            place = East(place)
        else:
            print("Not a valid direction!")
    if place == 32:
        print("You can travel: (N)orth or (S)outh.")
        direction = (input("Direction: ")).lower()
        if direction == "n":
            place = North(place)
        elif direction == "s":
            place = South(place)
        else:
            print("Not a valid direction!")
    if place == 22 or place == 33:
        print("You can travel: (S)outh or (W)est.")
        direction = (input("Direction: ")).lower()
        if direction == "s":
            place = South(place)
        elif direction == "w":
            place = West(place)
        else:
            print("Not a valid direction!")
    if place == 13:
        print("You can travel: (E)ast or (S)outh.")
        direction = (input("Direction: ")).lower()
        if direction == "e":
            place = East(place)
        elif direction == "s":
            place = South(place)
        else:
            print("Not a valid direction!")
    if place == 23:
        print("You can travel: (E)ast or (W)est.")
        direction = (input("Direction: ")).lower()
        if direction == "w":
            place = West(place)
        elif direction == "e":
            place = East(place)
        else:
            print("Not a valid direction!")
print("Victory!")
