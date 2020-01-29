command = ""
is_car_started = False

while True:
    command = input().lower()
    if command == "start":
        if is_car_started:
            print("Car already started.!!")
        else:
            is_car_started = True
            print("Car started")
    elif command == "stop":
        if not is_car_started:
            print("Car already stopped.!!")
        else:
            is_car_started = False
            print("Car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, i don't understand")
