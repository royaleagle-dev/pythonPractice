import pprint

message = "I am coming for you tonight"
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char]+1

pprint.pprint (count)
