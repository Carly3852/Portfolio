from random import *


#Create the list of words you want to choose from.
side_list = ["Roasted potatoes","Fries","Broccoli","carrots","Cesar Salad","Tofu","Rice"]
main_list = ["Griled chicken","Fish","Ceviche","Clam Soup","Pasta", "Tuna sandwhich", "Veg Sandwhich"]
dest_list = ["Flan","Nothing else remember your diet!","Cheesecake"]





#Generates a random integer.
sideR= randint(0, len(side_list)-1)
mainR= randint(0, len(main_list)-1)
destR= randint(0, len(dest_list)-1)
print(side_list[sideR] + " with " + main_list[mainR] + " and  " + dest_list[destR])
