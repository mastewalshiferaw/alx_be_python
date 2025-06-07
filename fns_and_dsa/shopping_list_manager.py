def display_menu():
  print("Shopping List Manager")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. View List")
  print("4. Exit")

def main():
  shopping_list = []
  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      user = input("What item you want to add: ")
      shopping_list.append(user)
      pass
    elif choice == '2':
      us= input("What item you want to remove: ")
      shopping_list.remove(us)
      pass
    elif choice == '3':
      print(f"{shopping_list[0:]}")
      pass
    elif choice == '4':
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()