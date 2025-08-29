todo_list = []
done = False

print("Type 'done' at any time to exit")

while not done:
    new_item = input("Add item to list: ")
    if new_item.lower() == "done":
        done = True
    else:
        todo_list.append(new_item) 

print(f"Here is your to-do-list {todo_list}")   
