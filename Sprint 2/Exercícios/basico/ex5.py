import json

with open('person.json', 'r') as person:
    pessoa = json.load(person)

print(pessoa)
