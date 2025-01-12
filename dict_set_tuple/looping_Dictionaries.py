# ==== Iterating over dictionaries =====

# dictionary.values()
# dictionary.keys()
# dictionary.items()



order_by_city = {
"London" : 200,
"Liverpool": 250,
"Manchester": 100,
"Bristol": 50
}


city_orders = list(order_by_city.items())

# print(order_by_city.keys())
# print(order_by_city.values())

for city,order in city_orders:
    print(order)


ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}

print(ski_runs.get('eas'))