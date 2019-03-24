import json as js

rubbish_data = (['Kuca'], ['Ulica', 'Grad', {'kljuc': 'vrednost'}])

json_rubbish_data = js.dumps(rubbish_data)

with open('dump_data.json', 'w') as file:
    js.dump(json_rubbish_data, file)

read_rubbish_data = js.loads(json_rubbish_data)
print(read_rubbish_data)

with open('dump_data.json', 'r') as filler:
    js.load(filler)
