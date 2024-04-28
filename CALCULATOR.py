import math
import subprocess


print ("Welcome to the field calculator!")
print ("Select which field you want to calculate!")
print (" ")
print ("1.square")
print ("2.triangle")
print ("3.rectangle")
print ("4.trapeze")
print ("5.wheel")
n = int(input("Just enter a number: "))
if n == 1:
    print ("You have chosen the area of ​​the square")
    print (" ")
    a = float(input("Enter the length of side 'a': "))
    p = a ** 2
    print("The area of ​​the square is",p,"cm2")
if n == 2:
    print ("You have chosen the area of ​​the triangle")
    print (" ")
    a = float(input("Enter the length of side 'a': "))
    h = float(input("Enter the height: "))
    p =( a / 2 ) * h
    print("The area of ​​the triangle is",p,"cm2")
if n == 3:
    print ("You have chosen the area of ​​the rectangle")
    print (" ")
    a = float(input("Enter the length of side 'a': "))
    b = float(input("Enter the length of side 'b': "))
    p = a * b
    print("The area of ​​the rectangle is",p,"cm2")
if n == 4:
    print ("You have chosen the area of ​​the trapeze")
    print (" ")
    a = float(input("Enter the length of side 'a': "))
    b = float(input("Enter the length of side 'b': "))
    h = float(input("Enter the height: "))
    p =  (( a + b ) * h) / 2
    print("The area of ​​the trapeze is",p,"cm2")

if n == 5:
    print ("You have chosen the area of ​​the wheel")
    print (" ")
    def pole_kola(r):
        return math.pi * r**2
    r = float(input("Enter the radius 'r': "))
    pole = pole_kola(r)
    print("The area of ​​the wheel is",pole,"cm2")

else:
    print ("Please enter the correct number!")
    subprocess.run(["python", "CALCULATOR.py"])        

