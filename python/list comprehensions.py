# list comprehensions = a way to create a new list with less syntax
#                       can mimic certain lambda function, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]

#squares = []
#for i in range(1,11):
    #squares.append(i * i)
#print(squares)

#squares = [i * i for  i in range(1,11)]
#print(squares)

students = [100,90,80,70,60,50,40,33,28,18,14,6]

#passed_students = list(filter(lambda x:x >= 33, students))

passed_students = [i if i >= 33 else "Failed" for i in students]

print(passed_students)