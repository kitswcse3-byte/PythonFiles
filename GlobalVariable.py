
counter = 0

def increment_counter():
    global counter  
    counter += 1
    print("Counter inside function:", counter)

def reset_counter():
    global counter
    counter = 0
    print("Counter has been reset.")

print("Initial Counter:", counter)
increment_counter() 
increment_counter()  
print("Counter after increments:", counter)

reset_counter()      
print("Final Counter:", counter)
