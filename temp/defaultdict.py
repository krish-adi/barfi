from collections import defaultdict
 
 
# Defining a dict
d = defaultdict(list)
 
for i in range(5):
    d[i].append(i)
     
print("Dictionary with values as list:")
print(d)

# Dictionary with values as list:
# defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})