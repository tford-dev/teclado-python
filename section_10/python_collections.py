"""
* counter
* defaultdict
* ordereddict
* nametuple
* deque
"""

"""
#Code below doesn't work
from collections import Counter
device_temperatures = [25.5, 26.0, 27.3, 24.8, 28.1, 26.7, 25.9, 27.5];
temperature_counter = Counter(device_temperatures);
print(temperature_counter([26.0]));
"""

from collections import defaultdict;

coworkers = [
    ("Alice", "Harvard University"),
    ("Bob", "Stanford University"),
    ("Charlie", "Massachusetts Institute of Technology"),
    ("Diana", "University of California, Berkeley")
];

alma_maters = defaultdict(list);

for coworker, place in coworkers:
    alma_maters[coworker].append(place);

#raises keyError if parameter/key is not existent in dictionary   
#alma_maters.default_factory = None;    
# print(alma_maters["Alice"]);
# print(alma_maters["terry"])

my_company = 'Ford Enterprise Solutions';
coworkers = ['Lee', 'Alex', 'Chase', 'Said'];
other_coworkers = [('Cynthia', 'Google'), ('Mike', 'NSA')];
coworker_companies = defaultdict(lambda: my_company);
for person, company in other_coworkers:
    coworker_companies[person] = company;
    
# print(coworker_companies[coworkers[0]]);
# print(coworker_companies['Cynthia']);

from collections import OrderedDict;

o = OrderedDict();
o["Ye"] = 6;
o["Kim"] = 12;
o["North"] = 3;

#print(o); #OrderedDict([('Ye', 6), ('Kim', 12), ('North', 3)])
# o.move_to_end("Ye")  # OrderedDict([('Kim', 12), ('North', 3), ('Ye', 6)])
# print(o);
# o.move_to_end("Kim", last=False);
# print(o); 
# o.popitem();
# print(o);

from collections import namedtuple
account = ('checking', 1850.90);
Account = namedtuple('Account', ['name', 'balance']);

account = Account('checking', 1850.90); 
# print(account.name); # checking
# print(account)  # Account(name='checking', balance=1850.9)
#accountNamedTuple = Account._make(account);
#print(accountNamedTuple); #Account(name='checking', balance=1850.9)
accountNamedTuple = Account(*account);
#print(accountNamedTuple._asdict()['balance']); #1850.9

from collections import deque;
friends = deque(("Kim", "Kylie", "Kendall", "Khloe"));
friends.append('Travis');
print(friends); # deque(['Kim', 'Kylie', 'Kendall', 'Khloe', 'Travis'])
friends.appendleft('Ye');
print(friends); #deque(['Ye', 'Kim', 'Kylie', 'Kendall', 'Khloe', 'Travis'])
friends.pop();
print(friends); #deque(['Ye', 'Kim', 'Kylie', 'Kendall', 'Khloe'])
friends.popleft();
print(friends); #deque(['Kim', 'Kylie', 'Kendall', 'Khloe'])