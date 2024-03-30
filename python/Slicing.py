# slicing = create a substring by extracting elements from another string
#            indexing[] or slicing[]
#            [start:stop:step]

name = "yeasin arafat"

first_name = name[0:]
last_name = name[0:]
funkey_name = name[::6]
reversed_name = name[::-1]

print(first_name)

website1 = "http://google.com"
website2 = "http://wikipdia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
