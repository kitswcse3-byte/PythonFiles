y = int(input("enter: "))
x = int(input("enter value:"))
print(f"addition of {x} and {y} is",(x+y))
print(f"addition of {x} and {y} is",(x-y))
print(f"addition of {x} and {y} is",(x*y))
print(f"addition of {x} and {y} is",(x/y))
print(f"addition of {x} and {y} is",(x%y))

print(f"{x} > {y} : ",x>y)
print(f"{x} < {y} : ",x<y)
print(f"{x} >= {y} : ",x>=y)
print(f"{x} <= {y} : ",x<=y)

print(f"bitwise and of {x},{y}",x&y)
print(f"bitwise or of {x},{y}",x|y)
print(f"not {y}",~y)

n1=list(input("Enter the list elements: "))
n2=int(input("Enter a number: "))
p=n1 in n2
if p:
    
    print(f"{n2} is in {n1}")
else :
    print(f"{n2} is not in {n1}")




