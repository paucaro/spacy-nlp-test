import json

with open('amazonjson.json', 'r', encoding='utf8') as f:
    data = json.load(f)

training_data = []
for example in data['examples']:
    temp_dict = {}
    temp_dict['text'] = example['basic_qualifications']
    temp_dict['entities'] = []
    for annotation in example['annotations']:
        start = annotation['start']
        end = annotation['end']
        label = annotation['tag_name'].upper()
        temp_dict['entities'].append((start, end, label))
    training_data.append(temp_dict)

print(training_data)