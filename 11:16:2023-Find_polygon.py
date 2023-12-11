# Logan White 11/16/2023
# 11:16:2023-Find_polygon.py
# Classwork - finds area of an inputed polygon 
# CC BY-NC-SA 4.0
# Variables
# Functions
def Choice():
    print("(1)\tA Triangle \n (2)\tA Rectangle \n (3)\tA Trapezoid \n (4)\tA Parallelogram \n ")
    """(5)\tA General Quadrilateral \n (6)\tA N-gon")"""
    print("Please Utilize The Number Assigned To The Shape")

    
def Triangle(units):
    width = float(input("Please Input The Width Of The Triangle \n"))
    height = float(input("Please Input The Height Of The Triangle \n"))
    print("Please Wait While We Calculate")
    volume = float((width*height)/2)
    print(f"The Volume is {volume} {units} Squared")


def Rectangle(units):
    width = float(input("Please Input The Width Of The Rectangle \n"))
    print("Please Input The Length Of The Rectangle \n")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float((width*height))
    print(f"The Volume is {volume} {units} Squared")


def Parallelogram(units):
    print("Please Input The Width Of The Parallelogram \n")
    width = float(input())
    print("Please Input The Height Of The Parallelogram \n")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float((width*height))
    print(f"The Volume is {volume} {units} Squared")


def Trapezoid(units):
    print("Please Input The First Base Of The Trapezoid \n")
    base_1 = float(input())
    print("Please Input The Second Base Of The Trapezoid \n")
    base_2 = float(input())
    print("Please Input The Height Of The Trapezoid")
    height = float(input())
    print("Please Wait While We Calculate")
    volume = float(((base_1+base_2)/2)*height)
    print(f"The Volume is {volume} {units} Squared")


"""
def General_quad(units):
    pass


def N-Gon(units):
    pass
    """

def AskShape():
    print("\nAre You Calculating The Volume Of:")
    Choice()
    return (input())
    

def AskUnit():
    print("\nPlease Confirm The Units Used For The Measurements Are The Same"
          "Then Input The Units Used For Measurements")
    return str(input())


def ShapeCheck(shape,units):
    if ("1" or "tri") in  shape.lower():
        print("Calculating Area Of Triangle")
        Triangle(units)
        print("Thank You")
        exit
    elif ("2" or "rec") in  shape.lower():
        print("Calculating Area Of Rectangle")
        Rectangle(units)
        print("Thank You")
        exit
    elif ("3" or "para") in  shape.lower():
        print("Calculating Area Of Parallelogram")
        Parallelogram(units)
        print("Thank You")
        exit
    elif ("4" or "trap") in  shape.lower():
        print("Calculating Area Of Trapezoid")
        Trapezoid(units)
        print("Thank You")
        exit
        """
    elif ("5" or "gen") in  shape.lower():
        print("Calculating Area Of A Generalized Qudrilateral")
        General_quad(units)
        print("Thank You")
        exit
    elif ("6" or "n" or "gon") in  shape.lower():
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

