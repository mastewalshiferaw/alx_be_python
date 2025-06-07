from datetime import datetime, timedelta 
def display_current_datetime():
  current_date = datetime.now()
  toprint = current_date.strftime("Current date and time: %Y-%m-%d %H:%M:%S")
  print (toprint)
display_current_datetime()
numr = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
  current_date = datetime.now()
  future_date = current_date + timedelta(days=numr)
  toprint = current_date.strftime("Future date: %Y-%M-%d")
  print(toprint)


calculate_future_date()