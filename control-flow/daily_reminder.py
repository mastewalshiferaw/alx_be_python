task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a high priority task thatrequire immediate attention!")
    else:
      print(f"Reminder: '{task}' is a high priority task that do not require immediate attention!")
  case "medium":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a medium priority task do it as soon as you have time!")
    else:
      print(f"Reminder: '{task}' is a medium priority task do it as you have time no rush")
  case "low":
     if time_bound == "yes":
       print(f"Note: '{task}' is a low priority task do it as you have a free time but don't forget the time bound")
     else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

