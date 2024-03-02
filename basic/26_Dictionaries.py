# 1. Dictionaries are used to store data values in KEY:VALUE pairs.
#    A dictionary is a collection which is ordered* (after python version 3.7), changeable and do not allow duplicates.

car = {
    "brand": "Ford",  # here, key is brand and value is Ford
    "name": "Mustang",
    "model": "Fastback",
    # "model": "Mach",
    "year": 1969,
}

print(car)
print(car["model"])  # accessing data by passing key.

# 2. what if we pass the key that does not exits
#    print(car["age"])   # KeyError: 'age' so if we use .get("key") method we get 'none' if key doesnt exist in dictionary

print(car.get("age"))  # it returns 'none'

#    if key doesnt exist in dictionary, we can also use get method to return default value

print(
    car.get("vintage", "yeah!")
)  # if 'vintage' doesnt exits as key, it returns 'yeah!' by default.

# 3. Updating the values of keys in dictionary
car["model"] = "Cobra"
print(car)

# 4. Adding another key:value to dictionary
car["country"] = "USA"
print(car)

# 5. Deleting the key:value pair form dictionary

del car["year"]
print(car)

# 6. Dictionary.pop("key","default") -> v, remove specified key and return the corresponding value.

p = car.pop("model")
print(f"key_value = {p}")
print(car)

# If the key is not found, return the default if given; otherwise, raise a KeyError.

p_default = car.pop("model", "not found")
print("returned default value=", p_default)
print(car)
