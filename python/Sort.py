# sort() method = used with lists
# sort() function = used with iterbles

#students = ["yeasin","Rifat","Asadduzaman","Hridoy","Sihab","Sojib"]
#students = ("yeasin","Rifat","Asadduzaman","Hridoy","Sihab","Sojib")
#students.sort()
#students.sort(reverse=True)
#sorted_students = sorted(students,reverse=True)
#for i in sorted_students:
    #print(i)

                               #level-2
students = [("yeasin","A+",86),
             ("Rifat","A-",70),
             ("Asadduzaman","B",63),
             ("Sojib","c",54),
            ("Hridoy","F",33),
            ("Sihab","D",45,),]

students2 = (("yeasin","A+",86),
             ("Rifat","A-",70),
             ("Asadduzaman","B",63),
             ("Sojib","c",54),
            ("Hridoy","F",33),
            ("Sihab","D",45,),)

age = lambda age:age[2]
students.sort(key=age,reverse=True)
sorted_studesnts2 = sorted(students2,key=age)
for i in sorted_studesnts2:
    print(i)


