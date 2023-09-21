friends = [
    {"name": "Kim Kardashian", "location": "Los Angeles, California"},
    {"name": "Khloé Kardashian", "location": "Calabasas, California"},
    {"name": "Kourtney Kardashian", "location": "Hidden Hills, California"},
    {"name": "Kendall Jenner", "location": "Beverly Hills, California"}
]

your_location = input("Where you is? ");
friends_nearby = [friend for friend in friends if friend['location']== your_location];

if any(friends_nearby):
    print("You are not alone");

