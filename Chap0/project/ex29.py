# -*- coding:UTF-8 -*-

people = 20 
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomend!")
	
if people < cats:
    print("Not many cats! The world is saved!")
	
if people < dogs:
    print("The world is dry!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: 
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
	
# 附加练习	
if True and False:
    print("True")
else:
    print("False")

if False or False:	
    print(" True ")
else:
    print("False")
	
if 3 == 3 and not ("testing" == "testing" or "Pyhong" == "Fun"):
    print("True")
elif  3 == 3 and not ("testing" != "testing" or "Pyhong" != "Fun"):
    print("False")
	
