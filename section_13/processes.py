'''
Hey!

In the next lecture, Windows or ARM Mac(M1, M2, etc) users might encounter a small issue.

Due to the way these systems work you must make sure that the code that starts a process is surrounded by if __name__ == "__main__".

Otherwise when we start new processes, those processes automatically start new processes, and those start new ones, and so on. Python will not allow this to happen, and as protection it requires the above if statement.

So in the next video, when you see something like process.start(), make sure to do:

if __name__ == "__main__":
    process.start()
    ...
    process.join()
It's important that all the code in between starting the process and joining the process is inside the if statement.

Kind regards,

Jose
'''
import time
from multiprocessing import Process

def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

process = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)

if __name__ == "__main__":
    process.start()
    process2.start()

start = time.time()

if __name__ == "__main__":
    process.join()
    process2.join()

print(f'Two process total time: {time.time() - start}')

# import time
# from concurrent.futures import ProcessPoolExecutor

# def ask_user():
#     start = time.time()
#     user_input = input("Enter your name: ")
#     greet = f'Hello, {user_input}'
#     print(greet)
#     print(f'ask_user, {time.time() - start}')


# def complex_calculation():
#     start = time.time()
#     print('Started calculating...')
#     [x**2 for x in range(20000000)]
#     print(f'complex_calculation, {time.time() - start}')


# start = time.time()
# ask_user()
# complex_calculation()
# print(f'Single thread total time: {time.time() - start}')

# start = time.time()

# with ProcessPoolExecutor(max_workers=2) as pool:
#     pool.submit(complex_calculation)
#     pool.submit(complex_calculation)

# print(f'Two process total time: {time.time() - start}')
