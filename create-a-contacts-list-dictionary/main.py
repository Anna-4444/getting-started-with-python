people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]
company_org = {}

for i in range(len(people)):
    person = people[i]
    person_title = title[i]


    company_org[person] = person_title

# print(company_org)


class PersonalAssistant:
    def __init__(self):
        self.contacts = company_org
        self.todos = []

    def get_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "No contact with that name"


assistant = PersonalAssistant()
print(assistant.get_contact("Nichole"))


