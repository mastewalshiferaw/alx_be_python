FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
  
def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  

choice = float(input("Enter the temperature to convert: "))
ist = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
ist = ist.lower()

if ist == 'c':
  result = convert_to_fahrenheit(choice)
  print(f"{choice:.1f}°C is {result:.1f}°F")
elif ist  == 'f':
  fah = convert_to_celsius(choice)
  print(f"{choice:.1f}°F is {fah:.1f}°C")
else:
  print("Invalid temperature. Please enter a numeric value.")

