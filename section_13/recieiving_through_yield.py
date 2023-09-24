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
        
def greet(g):
    #yield from g ... doing it this way is frowned upon
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)
        
greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello there')