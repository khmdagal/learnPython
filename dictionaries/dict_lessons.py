# when we want to create a dictionary in Python we use curly braces

cars = {
    "make": "Audi",
    "Model": "200A",
    "Year": "2023",
    'make': 'Audi'
    
}



# ===== Invalid Key =====

# ['yes']: 'yes' this key is not valid key  TypeError: unhashable type: 'list'



# == updating existing key-value pairs and adding new onces.

# cars["make"] = 'Nissan'  
# We changed make from Audi to Nissan




cars['color'] = 'Gray'
# Now we created new key-value pair, color key and it's value was not existing in the original dictionary.

# === unique key ====

# In the above dictionary we have two key names that is the same 'make' with different values,
# When we run, we get no errors but the last one will override the first.

print(cars)



