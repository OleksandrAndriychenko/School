import json
new_dict = {100000: ('Tom', 24),
            100001: ('Bob', 42),
            100002: ('Sam', 34),
            100003: ('Oliver', 47),
            100004: ('Harry', 18),
            100005: ('Oscar', 21)}
with open('Hw_18.json', 'w') as file:
    json.dump(new_dict, file)