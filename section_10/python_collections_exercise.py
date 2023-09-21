from collections import defaultdict, OrderedDict, namedtuple, deque;

def create_defaultdict():
    my_defaultdict = defaultdict(lambda:"Unknown");
    my_defaultdict["Alan"] = "Manchester";
    return my_defaultdict;

result = create_defaultdict();
print(result);

def manipulate_ordered_dict(arg_od):
    #Remove the first and last entry in arg_od
    arg_od.popitem(last=False) #Remove the first entry
    arg_od.popitem() #Remove the last entry
    #Move the entry with key name "Kim" to the end of arg_od
    arg_od.move_to_end("Kim");
    #Move the entry with key name "Ye" to the start of arg_od
    arg_od.move_to_end("Ye", last=False);

my_ordered_dict = OrderedDict([('Travis', 1), ('Kim', 2), ('Kylie', 3), ('Ye', 4), ('Khloe', 5)]);
manipulate_ordered_dict(my_ordered_dict);
print(my_ordered_dict);

#Create a namedtuple type called "Player" with fields "name" and "club"
Player = namedtuple('Player', ['name', 'club']);

def create_player(name_arg, club_arg):
    #Create a Player namedtuple instance with the specified name and club
    player_instance = Player(name=name_arg, club=club_arg);
    #Return the Player namedtuple instance
    return player_instance;

player1 = create_player('Garret Reynolds', 'Fiend BMX');
print(player1.name);
print(player1.club);

def manipulate_deque(arg_deque):
    #Remove the last element in the deque
    arg_deque.pop();
    #Move the first element to the end
    first_element = arg_deque.popleft();
    arg_deque.append(first_element);
    #Add an element "Yeezy" to the start
    arg_deque.appendleft("Yeezy");

my_deque = deque(['Travis', 'Kim', 'Kylie', 'Ye']);
manipulate_deque(my_deque);
print(my_deque);