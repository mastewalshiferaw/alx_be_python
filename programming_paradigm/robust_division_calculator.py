def safe_divide(numerator, denominator):
  try:
    result = float(numerator)/float(denominator)
  except ValueError:
    if float(numerator) & float(denominator) == str:
      return "Error: Please enter numeric values only."

  except ZeroDivisionError:
    
      return "Error: Cannot divide by zero."
  else:
      return f"The result of the division is {result:.1f}"
  
      


  