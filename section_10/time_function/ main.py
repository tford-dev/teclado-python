import time, timeit;

def measure_runtime(func):
    start = time.time();
    func();
    end = time.time();
    return end - start;

def powers(limit):
    return [x**2 for x in range(limit)];

print(measure_runtime(lambda : powers(5)));