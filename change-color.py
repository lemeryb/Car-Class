from main import Car

paint_car = input("Enter the color you want the car to be painted: ").title()
car = Car("Tesla","S",paint_car,"2019","$60,000","0")
car.print_description()


