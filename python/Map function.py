# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)

store_BDT = [("4copy picture",80.00),
         ("6copy picture",105.00),
         ("8copy picture",130.00),
         ("10copy picture",155.00)]

to_dollaars = lambda data: (data[0],data[1]/110.75)
to_taka = lambda data: (data[0],data[1]*110.75)
store_USD = list(map(to_dollaars,store_BDT))
store_bd = list(map(to_taka,store_BDT))
for i in store_bd:
    print(i)