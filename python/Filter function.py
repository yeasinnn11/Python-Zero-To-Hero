# filter function() = creates a collection of elements from a iterable for which a function returns true
# (function and iterable)

friends = [("yeasin",19),
           ("Rifat",20),
           ("Hasan",17),
           ("Nayem",16),
           ("Asad",21),
           ("Rafi",22)]

party = lambda friends:friends[1] >= 18

chill = list(filter(party, friends))

for i in chill:
    print(i)