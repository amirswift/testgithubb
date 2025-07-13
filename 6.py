#ghodrat
def dianasour(name):
    if name == "trex":
        print("gosshtkhar")
 
def esm(name):
    print("hello "+name+" welcome to this site")

def movie(name):
    if name == "trex":
        print("jurasic park")

def option(choice):
    if choice == "yes":
        print("ok")
    else:
        print("ok bye")

        
name1 = input("Please enter your name: ")
esm(name1)
dia = input("Please enter your dianasour: ")
dianasour(dia)
choice = input("Do you want to know movies of this? ")
movie(dia)