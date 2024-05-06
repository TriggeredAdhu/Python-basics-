# Project 2:
# Traffic light simulator

# python program to identify the traffic signal indications

color = (input("enter the traffic light to identify its indications"))

if color == "red":
    print("stop")

elif color == "yellow":
    print("proceed with caution")

elif color == "green":
    print("go")

else:
    print("invalid color, please enter a valid traffic color")

    