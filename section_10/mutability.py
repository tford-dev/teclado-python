friends = [
    {"name": "Kim Kardashian", "location": "Los Angeles, California"},
    {"name": "Khloé Kardashian", "location": "Calabasas, California"},
    {"name": "Kourtney Kardashian", "location": "Hidden Hills, California"},
    {"name": "Kendall Jenner", "location": "Beverly Hills, California"}
]

def get_id(list_arr):
    return id(list_arr);

#print(get_id(friends));

#below has the same id
opps = ["drake", "nike"];
print(get_id(opps));
opps.append("small-hats");
print(get_id(opps));