#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:08:10 2018

@author: jsantos
"""
print("This program converts a temperature from Celsius to Fahrenheit or vice-versa.")
selection = input("Enter C for Celsius or F for Fahrenheit: ")
select = selection.upper()

if select == 'C':
    celsius = input("Enter a temperature in Celsius: ")
    temperature = int(celsius) * 9/5 + 32
    #print("Your temperature in Fahrenheit is {t:1.2f}".format(t=temperature))
    print(f"Your temperature in Fahrenheit is: {temperature:1.2f}")
elif select == 'F':
    fahrenheit = input("Enter a temperature in Fahrenheit: ")
    temperature = (int(fahrenheit)-32) * 5/9
    #print("Your temperature in Celsius is {t:1.2f}".format(t=temperature))
    print(f"Your temperature in Celsius is: {temperature:1.2f}")
else:
    print("Error:  The letter you entered was not a 'C' or a 'F'")
