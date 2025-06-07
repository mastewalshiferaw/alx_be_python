FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  convert=FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit-32)
  return convert
def convert_to_fahrenheit(celsius):
  convert = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius + 32)
  return convert

choice = float(input("Enter the temperature to convert: "))
ist = input("Is this temerature in Celsius or Fahrenheit? (c/f): ").lower()

if ist == 'c':
  sum = convert_to_fahrenheit(choice)
  print(f"{choice:.1f}°C is {sum:.1f}°F")
elif ist  == 'f':
  fah = convert_to_celsius(choice)
  print(f"{choice:.1f}°F is {fah:.1f}°C")
else:
  print("Invalid temperature. Please enter a numeric value")

