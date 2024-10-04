# -*- coding: utf-8 -*-
"""temperature_conversion

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CZJSOVKW0xNu4N-1LykWAlxxjStKe4pM
"""

#python program to convert temperature between Fahrenheit and Celsius

#converts a temperature from celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

#converts a temperature from fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

#use is prompted to choose between converting Celsius to Fahrenheit or Fahrenheit to Celsius
def main():
  temperature_type = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ")
  temperature_type = temperature_type.upper()
  if temperature_type == 'C':
    celsius  = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} is equal to {fahrenheit:.2f} in Fahrenheit")
  elif temperature_type == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} is equal to {celsius:.2f} in Celsius")
  else:
    print("Invalid input. Please enter 'C' or 'F'.")
    main()
#call the main function
if __name__ == '__main__':
  main()