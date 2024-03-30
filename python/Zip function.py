# zip (*iterables) = aggregate from tow or more iterables (list, tuples, sets, etc.)
#                    create a zip object with paired elements store in tuples for each elements

username = ["Arafat","Yeasinnn","Hafsa","Saad"]
passwords = ["@araf@t","@yeasin11","h@fs@","S@@d"]
login_date = ["9/10/2006","11/10/2005","10/10/2025","09/10/2026"]

#user = dict(zip(username,passwords))
#print(type(user))
#for key,value in user.items():
    #print(key+" : "+value)

user = zip(username,passwords,login_date)

for key,value,date  in user:
    print(key+" : "+value+" - "+date)