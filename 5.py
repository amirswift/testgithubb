def ranandegi(soraat):
    if soraat> 100:
        print("You can not drive like this")
    elif soraat<=100 and soraat>60:
        print("This speed is perfect")
    elif soraat < 60:
        print("Move faster")
    else:
        print("Dont drive")

speed = int(input("Please enter your speed: "))
ranandegi(speed)