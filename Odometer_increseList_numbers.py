"""Write a function roll_odometer that adds 1 to a number represented
by a list of digits, carrying where appropriate, e.g.:
    roll_odometer([1, 0, 2]) = [1, 0, 3]
    roll_odometer([1, 3, 9, 9]) = [1, 4, 0, 0]
    roll_odometer([9, 9, 9]) = [0, 0, 0] (resets like an odometer)"""


def odometer(roll_odometer):
    """
    :arg
        roll_odometer (list): contained integer values.
        b(string): b is having all the values of list mapped as a single string.
        b(integer): string b is converted into number and its value increased by one.
        b(string): integer type b is converted into string so that we can convert it into list.
        a(string): string type removing extra digits after incrementing values
        c(list): list of integer values after processing.

    :returns
        c(list): Final result of the odometer.
    """

    b="".join(map(str,roll_odometer[0:]))
    b=int(b)+1
    b=str(b)
    if len(b)>len(roll_odometer):
        a = "".join(b[1:])
    else:
        a = "".join(b[0:])
    c=list(map(int,a))
    return 'Values after Reset' , {'roll_odometer' :c}

"""
n(integer): Taking numer of values from user
a(integer): values in list
obj(object): function call  
"""
roll_odometer=[]
n=int(input("Enter the no of values as Input in roll_odometer[] : "))
print("Enter the values")
for i in range(n):
    a=int(input())
    roll_odometer.append(a)
print("roll_odometer: ",roll_odometer)
obj=odometer(roll_odometer)
print(*obj)

