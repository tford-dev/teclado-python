# roll_combinations = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
# print(roll_combinations);
#[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

#We can do the same thing with the code below
from itertools import product;
#dice_combos =  product(range(1, 7), repeat=2); returns generator
dice_combos =  list(product(range(1, 7), repeat=2));
print(dice_combos); 

print("...........................................................................");

list_1 = ["a", "b", "c"];
list_2 = [1, 2, 3];
#cartesian_product = product(list_1, list_2); returns a generator
cartesian_product = list(product(list_1, list_2));
print(cartesian_product);

print("...........................................................................");

from itertools import permutations;
#but we can use the optional r parameter to limit the function to finding shorter permutations.
p_1 = list(permutations("ABC", r=2));
print(p_1);

print("...........................................................................");

from itertools import combinations, combinations_with_replacement;
#r argument is mandatory
c_1 = list(combinations("ABC", r=2));
c_2 = list(combinations("ABC", r=3));
c_3 = list(combinations((1, 2, 3, 1), r=2));
print(c_1); #('A', 'B'), ('A', 'C'), ('B', 'C')]
print(c_2); #[('A', 'B', 'C')]
print(c_3); #[(1, 2), (1, 3), (1, 1), (2, 3), (2, 1), (3, 1)]

c_4 = list(combinations((1, 2, 3), r=2)); #[(1, 2), (1, 3), (2, 3)]
#c_5 matches every element to itself
c_5 = list(combinations_with_replacement((1, 2, 3), r=2)); #[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
print(c_4);
print(c_5);
print("...........................................................................");