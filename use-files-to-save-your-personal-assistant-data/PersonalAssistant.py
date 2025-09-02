people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]
company_org = {}

for i in range(len(people)):
    person = people[i]
    person_title = title[i]


    company_org[person] = person_title

# print(company_org)


class PersonalAssistant:
    def __init__(self, todos):
        # self.contacts = company_org
        self.todos = todos

    def add_todo(self, new_item):
        self.todos.append(new_item)

    def remove_todo(self, todo_item):
        if todo_item in self.todos:
            index = self.todos.index(todo_item)
            self.todos.pop(index)
        else:
            print("Todo is not in list!")
        # for i in range(len(self.todos)):
        #     if todo_item == self.todos[i]:
        #        return self.todos.pop(i)        
        # print("Todo is not in list!")

    def get_todos(self):
        return self.todos

    def get_birthday(self, name):
        if name == "Nate":
            print("Birthday is 02/23/82!")
        elif name == "Lucy":
            print("Birthday is 01/07/10!")
        elif name == "Sam":
            print("Birthday is 07/22/12!")
        else:
            print("Can't find a birthday for this person...")

    def get_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "No contact with that name"

# assistant = PersonalAssistant()
