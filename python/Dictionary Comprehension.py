# Dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda function

#dictionary = {kye: expression for (key,value)in iterable}
#dictionary = {kye: expression for (key,value)in iterable if conditional}
#dictionary = {kye: (if/else) for (key,value)in iterable}
#dictionary = {kye: function(value) for (key,value)in iterable}
#----------------------------------------------------------------
#cities_in_F ={"Dhaka":88,"Sylhet":68,"Chittagong":94,"Khulna":45,"Rongpur":75}
#cities_in_C ={key: round((value-32)* (5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)

#------------------------------------------------------------------
#weather = {"Dhaka":"Hot","Sylhet":"snowing","Chittagong":"cloud","Khulna":45,"Rongpur":"Hot"}
#hot_weather = {key: value for (key,value) in weather.items() if value =="Hot"}
#print(hot_weather)

#--------------------------------------------------------------------
#cities = {"Dhaka":88,"Sylhet":26,"Chittagong":94,"Khulna":32,"Rongpur":75}
#desc_cities = {key: ("warm" if value >= 33 else "Cold")for (key,value) in cities.items()}
#print(desc_cities)

#--------------------------------------------------------------------
def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >=33:
        return "warm"
    else:
        return "Cold"

cities = {"Dhaka":88,"Sylhet":26,"Chittagong":94,"Khulna":32,"Rongpur":75,"Maymensing":56}
desc_Cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_Cities)