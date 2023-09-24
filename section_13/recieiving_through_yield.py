# def greet():
#     friend = yield
#     print(f'Hello, bitch ass {friend}')
    
# g = greet()
# g.send(None) #Priming the generator

# g.send('Khloe')

from collections import deque

friends = deque(('Kim', 'Ye', 'Kylie', 'Travis', 'Khloe', 'Tristan'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')