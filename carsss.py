# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:38:52 2023

Github Account:misskankam
Github link;

6939121
@author: abena
"""

#list of available cars 
cars= {
"Audi":850000,
"Tesla":100000,
"Toyata vitz": 11000,
"Honda Civic":32000,
"Toyota Corolla":65000,
"Ford Mustang":88000, 
"Toyota Yaris":15000,
"Jeep Wrangler":985000,
"Ford Explorer":75000,
"G Wagon":890000,
"Ford GT":560000,
"Nissan Altima":45000,
"Sentra":34000,
"Hyundai Elantra":79000,
"Ford EcoSport":66000,
"Prado Landcruiser":899000, 
"Land Rover Defender 2002":545000,
"Range Rover":975500,
"Bentley": 995500,
"Nissan Titan suv": 89000,
"Jagua suv":78000,
"Peugeot":79000,
"Pajero mitsubishi":70000,
"Mercedes benz":999000,
"BMW mini cooper":89000,
"Jeep cherokee":99000,
"Hyundai tucson ":68000,
"Honda CRV":767000,
"Suzuki swift":67600,
"Lexus":895000,
}
#get user input for car name
car_name=input("Enter your car name:")
#check if car name is in the list of available cars
if car_name in cars:
    print("Yes")
    #if car name is present, get its price 
    car_price=cars[car_name]
    print(f"The price of {car_name} is ${car_price}.")
else:
    #if car name is not present, inform the user 
    print(f"Sorry,{car_name} is not available")
    