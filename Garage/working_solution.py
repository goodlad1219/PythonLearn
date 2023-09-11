import json

data = open("sheet.json")
data_dictionary = json.load(data)
print(data_dictionary)
current_day = "Monday"
filter_list = data_dictionary["Monday"]
acounts = []

for i in filter_list:
    print(type(i))

print()