from collections import OrderedDict

string = "AABCBBABBAC"
newdict = OrderedDict.fromkeys(string, 1)
print(newdict.keys())
print(newdict.items)


#! But After python 3.7 regular dictionaries also maintain orders so,no need to insert extra package

new_dict = dict.fromkeys(string)
print(new_dict)
