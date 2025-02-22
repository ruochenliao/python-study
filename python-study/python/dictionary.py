my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(my_dict)
print(my_dict["brand"])
print(my_dict.get("brand"))
print()
for x in my_dict:
    print(x)

print()
for x in my_dict.keys():
    print(x)

print()
for x in my_dict.values():
    print(x)

print()
for x,y in my_dict.items():
    print(x,y)


# before keys()
x = my_dict.keys()
print(x)

# after keys()
my_dict["color"] = "yellow"
print(x)


my_dict.pop("color")
print(my_dict)

del my_dict["model"]
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# copy
new_dict = my_dict.copy()
print(new_dict)
new_dict = dict(my_dict)
print(new_dict)