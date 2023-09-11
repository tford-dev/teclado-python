def greet():
    print("Hello World");

def before_and_after(func):
    print("Before...");
    func();
    print("After...");

#before_and_after(greet);

kanye_west_albums = [
    {"name": "The College Dropout", "executive_producer": "Kanye West"},
    {"name": "Late Registration", "executive_producer": "Kanye West"},
    {"name": "Graduation", "executive_producer": "Kanye West"},
    {"name": "808s & Heartbreak", "executive_producer": "Kanye West"},
    {"name": "My Beautiful Dark Twisted Fantasy", "executive_producer": "Kanye West"},
    {"name": "Yeezus", "executive_producer": "Kanye West"},
    {"name": "The Life of Pablo", "executive_producer": "Kanye West"},
    {"name": "Ye", "executive_producer": "Kanye West"},
    {"name": "Jesus Is King", "executive_producer": "Kanye West"},
    {"name": "Donda", "executive_producer": "Kanye West"}
]

# def find_album(expected, finder, list_arr):
#     for album in list_arr:
#         try:
#             if finder(album).lower() == expected.lower():
#                 return album;
#         except AttributeError:
#             if finder(album) == expected:
#                 return album;
def find_album(expected, finder, list_arr):
    found = [];
    for album in list_arr:
        if finder(album) == expected:
            found.append(album);
    return found;

find_by = input("What property are we searching by? "); #this is to find a key in a dictionary
looking_for = input("What are you looking? ");
album_lookup = find_album(looking_for, lambda album: album[find_by], kanye_west_albums);
print(album_lookup or 'No albums found.');