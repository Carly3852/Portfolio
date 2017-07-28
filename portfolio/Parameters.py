operation = input("What do you want to find?\n")
operation= operation.lower()

if (operation == "volume"):
    B=int(input("What is the width of the figure?\n"))
    AL=int(input("What is the height? \n"))
    D= int(input("what is the lenght? \n"))
    def V(W, H, L):
        vol = W*H*L
        return vol
    print( "The Volume of your figure is " + (V(B, AL,D))

if (operation == "area" ):
    B=int(input("What is the width of the figure?\n"))
    AL=int(input("What is the height? \n "))
    def A(W, H):
        area = W * H
        return area
    print("The Area of your figure is " + A(B,AL))
