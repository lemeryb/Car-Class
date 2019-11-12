from main import Car
import time
mileage = 0

begin_driving = int(input("Would you like to begin driving your new car?\nPress 1 to drive.\nPress 2 to exit."))

if begin_driving == 1:
    print("Starting the car..")
    while mileage < 3:
        time.sleep(1)
        mileage += 1
        print("Miles Driven: " + str(mileage))
    car = Car("Tesla","S","Green","2019","$60,000",str(mileage))
    car.print_description()
elif begin_driving == 2:
    exit()
