# Title Car Class
# Author: Benjamin Lemery
# Date: 11/11/19
# This program demonstrates how to use classes.
# README: Start the program from change-color.py and/or odometer_increment.py


class Car:

    def __init__(self,make,model,color,year,price,mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.mileage = mileage

    def print_description(self):
        print("Manufacturer: " + self.make)
        print("Model: " + self.model)
        print("Color: " + self.color)
        print("Year: " + self.year)
        print("Price: " + self.price)
        print("Mileage: " + self.mileage)

car = Car("Tesla","S","Green","2019","$60,000","0")
car.print_description()




