# **kwargs = parameter that will pack al arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello "+kwargs['first']+kwargs["middle"]+kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Yeasin",middle=" Arafat ",last="code")