from collections import deque
from types import coroutine

friends = deque(('Kim', 'Ye', 'Kylie', 'Travis', 'Khloe', 'Tristan'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print("Starting Process...")
    await g #... doing it this way is frowned upon
    print("Terminating Process...")
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)



greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello, Darkness my old friend, and you, ')
greeter.send('Hello, Darkness my old friend, and you, ')
greeter.send('Hello, Darkness my old friend, and you, ')
greeter.send('Hello, Darkness my old friend, and you, ')
greeter.send('Hello, Darkness my old friend, and you, ')
greeter.send('Hello, Darkness my old friend, and you, ')
