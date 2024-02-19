def help():
    print(
        """Commands : 
                1. Start: To start the car 
                2. Stop: To stop the car 
                3. Quit: To quit the game 
                4. Help: To ask for guidebook """
    )

    # 1-start  0-stop


command = ""
n = 0
while 1:
    command = input(">>").lower()
    if command == "start":
        if n == 0:
            print("Car Started...")
            n = 1
        else:
            print("Car has already Started...")
    elif command == "start" and n == 1:
        print("Car has already Started...")
    elif command == "stop":
        if n == 1:
            print("Car Stopped.")
            n = 0
        else:
            print("Car has not started yet.")
    elif command == "help":
        help()
    elif command == "quit":
        break
    else:
        print("I dont understand.")
