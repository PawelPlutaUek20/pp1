from collections import Counter
import json
import re

with open('DontMakeMeWait.txt') as f:
    data = f.read()
    letters = re.findall('[a-zA-Z]', data)
    sorted(letters)
    str_letters = ''.join(letters)
    amount_letters = Counter(str_letters.lower())
    

with open('counter.json', 'w') as f:
    json.dump(amount_letters, f, indent=4)