#Logan White 11/16/2023
#11/16/2023-Find_polygon.py
#Classwork finds area of an inputed polygon 
#CC BY-NC-SA 4.0
#Variables
#Functions
def Choice():
    print("(1)\tA Triangle")
    print("(2)\tA Rectangle")
    print("(3)\tA Trapezoid")
    print("(4)\tA Parallelogram")
    """
    print("(5)\tA General Quadrilateral")
    print("(6)\tA N-gon")"""
    print("Please Utilize The Number Assigned To The Shape")

    
def Triangle(units):
    print("Please Input The Width Of The Triangle")
    width = float(input())
    print("Please Input The Height Of The Triangle")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float((width*height)/2)
    print("The Volume is " + str(volume) + " " + units + " Squared")
def Rectangle(units):
    print("Please Input The Width Of The Rectangle")
    width = float(input())
    print("Please Input The Length Of The Rectangle")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float((width*height))
    print("The Volume is " + str(volume) + " " + units + " Squared")
def Parallelogram(units):
    print("Please Input The Width Of The Parallelogram")
    width = float(input())
    print("Please Input The Height Of The Parallelogram")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float((width*height))
    print("The Volume is " + str(volume) + " " + units + " Squared")
def Trapezoid(units):
    print("Please Input The First Base Of The Trapezoid")
    base_1 = float(input())
    print("Please Input The Second Base Of The Trapezoid")
    base_2 = float(input())
    print("Please Input The Height Of The Trapezoid")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float(((base_1+base_2)/2)*height)
    print("The Volume is " + str(volume) + " " + units + " Squared")
"""
def General_quad(units):

def N-Gon(units):

    """

def AskShape():
    print("\nAre You Calculating The Volume Of:")
    Choice()
    return (input())
    
def AskUnit():
    print("\nPlease Confirm The Units Used For The Measurements Are The Same")
    print("Then Input The Units Used For Measurements")
    return str(input())

def ShapeCheck(shape,units):
    if shape.lower().__contains__("1"):
        print("Calculating Area Of Triangle")
        Triangle(units)
        print("Thank You")
        exit
    elif shape.lower().__contains__("2"):
        print("Calculating Area Of Rectangle")
        Rectangle(units)
        print("Thank You")
        exit
    elif shape.lower().__contains__("3"):
        print("Calculating Area Of Parallelogram")
        Parallelogram(units)
        print("Thank You")
        exit
    elif shape.lower().__contains__("4"):
        print("Calculating Area Of Trapezoid")
        Trapezoid(units)
        print("Thank You")
        exit
        """
    elif shape.lower().__contains__("5") or "Gen" in shape:
        print("Calculating Area Of A Generalized Qudrilateral")
        General_quad(units)
        print("Thank You")
        exit
    elif shape.lower().__contains__("6") or "n-gon" in shape:
        print("Calculating Area Of N-Gon")
        N-Gon(units)
        print("Thank You")
        exit"""
    else:
        print("Please Input A Proper Option Of ")
        Choice()
        main()

def main():
    units = AskUnit()
    shape = AskShape()
    ShapeCheck(shape,units)
#Code
main()

