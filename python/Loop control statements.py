# loop control statemnets = change a loops execution from its normal sequence

# break    = used to terminate the loop entirely
# continue = skip to the next iteration of the loop
#pass      = does nothing, acts as a plaseholder

#while True:
    #name = input("Enter your name: ")
    #if name != "" :
     #break
phone_number = "123-456-789"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i,end="")

for i in range(1,21+1):
    if i == 13:
        pass
    else:
        print(i)