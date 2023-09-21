def hundred_numbers():
    i = 0;
    while i < 100:
        yield i;
        i += 1;
        
g = hundred_numbers();
#print([x + 1 for x in g]); """no zero"""
#print([x for x in hundred_numbers()]);
#print([x * 2 for x in hundred_numbers()]);
print(next(g));
print(list(g));