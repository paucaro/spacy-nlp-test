from deep_translator import GoogleTranslator
import json

translated = GoogleTranslator(source='auto', target='es').translate("keep it up, you are awesome")
print(translated)

with open('amazonjson.json', 'r', encoding='utf8') as f:
    data = json.load(f)

i = 0
for example in data['examples']:
    basic_q_tr = GoogleTranslator(source='auto', target='es').translate(example['basic_qualifications'])
    preferred_q_tr = GoogleTranslator(source='auto', target='es').translate(example['preferred_qualifications'])
    data['examples'][i].update({"basic_qualifications":basic_q_tr})
    data['examples'][i].update({"preferred_qualifications":preferred_q_tr})
    i += 1