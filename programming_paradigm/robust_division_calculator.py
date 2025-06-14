def safe_divide(numerator, denominator):
  try:
    result = numerator/denominator
  except ZeroDivisionError:
    if denominator == 0:
      print("Error: Cannot divide bt zero.")
    else:
      print (f"The result of the division is {result}")
  except ValueError:
    if numerator & denominator == str:
      print("Error: Please enter numeric values only.")
      


  