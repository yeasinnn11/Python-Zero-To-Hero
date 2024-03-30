import time

#print(time.ctime(10000000))   #convert a time express in seconds since epoch to a readable string
#                              epoch = when your computer thinks time began (reference point)

#print(time.time())  # return current second's since epoch

#print(time.ctime(time.time()))

time_object = time.localtime() # local time
time_object = time.gmtime() #UTC time
print(time_object)
locale_time = time.strftime("%B %D %Y %H:%M:%S", time_object)
print(locale_time)

