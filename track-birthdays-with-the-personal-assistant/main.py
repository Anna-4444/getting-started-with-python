#imports PersonalAssistant.py file
import json
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)

  assistant = PersonalAssistant(todo_list, birthday_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list

    **** Birthdays ****
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    # Get Birthday
    elif user_command == "4":
        print(f"\nYour Birthday Contacts")
        print(assistant.get_birthdays())     
        user_input = input("Whos birthday would you like to get? ")
        print(assistant.get_birthday(user_input))
    # Add Birthday
    elif user_command == "5":
        name = input("Name of the person: ")
        birthday = input("Their birthday (ex: 08/18/2000): ")
        print(assistant.add_birthday(name, birthday))

    # Remove Birthday
    elif user_command == "6":
        print(f"\nYour Birthday Contacts")
        print(assistant.get_birthdays())     
        user_input = input("Whos birthday would you like to remove? ")
        print(assistant.remove_birthday(user_input))

    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

with open("birthdays.json", "w") as birthdays:
    json.dump(assistant.get_birthdays(), birthdays)

with open("todo.json", "w") as write_todos:
    json.dump(assistant.get_todos(), write_todos)