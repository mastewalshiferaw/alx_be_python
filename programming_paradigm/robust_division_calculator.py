def safe_divide(numerator, denominator):
  try:
    result = float(numerator)/float(denominator)
  except ZeroDivisionError:
    if float(denominator) == 0:
      print("Error: Cannot divide by zero.")
    else:
      print (f"The result of the division is {result:.1f}")
  except ValueError:
    if float(numerator) & float(denominator) == str:
      print("Error: Please enter numeric values only.")
      


  