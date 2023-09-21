def starts_with_t(friend):
    return friend.startswith('t');

friends = ['khloe', 'ye', 'travis', 'kylie', 'tristan', 'kim'];
start_with_t = filter(starts_with_t, friends); #arg 1: function that returns true/false
# print(next(start_with_t));
# print(next(start_with_t));
# print(list(start_with_t)); #blank

friends_upper = map(lambda x: x.upper(), friends);
#friends_upper = [friend.upper() for friend in friends];
#print(friends_upper);
# print(next(friends_upper));
# print(next(friends_upper));
# print(next(friends_upper));

class User: 
    def __init__(self, username, password):
        self.username = username;
        self.password = password;
    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password']);
    
users = [
    {'username':'terry', 'password': 'cisco'},
    {'username': 'ross', 'password': 'pinq'}
];

#users = [User.from_dict(user) for user in users];
users = map(User.from_dict, users);

print(list(users));