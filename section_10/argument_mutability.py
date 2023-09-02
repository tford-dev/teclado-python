friends_last_seen = {
    'Kendall' : 31,
    'Travis' : 1,
    'Khloe' : 7
};

def see_friends(friends, name):
    print(id(friends));
    friends[name] = 0;
    
# print(id(friends_last_seen));
# print(id(friends_last_seen['Kendall'])); #different id

# see_friends(friends_last_seen, 'Kendall');

# print(id(friends_last_seen['Kendall']))  #different id
# print(id(friends_last_seen));

age = 20;

def increase_age(current_age):
    current_age = current_age + 1;
#age variable is an integer, integers are not mutable. look at how ids did not change 
# print(id(age));
# increase_age(age);
# print(id(age));

primes = [2, 3, 5];
print(id(primes));

primes += [7, 11]; #this appends to original primes list?
print(id(primes));