print("Normal Calculator")

a = float(input("enter first no."))
b = float(input("enter second no."))

print("select operations")
print("1. addition(+)")
print("2. substraction(-)")
print("3. multiplication(*)")
print("4. division(/)")

choice = input("enter choice(+,-,*,/)")

if choice == "+":
    print("result", a + b)
    
elif choice == "-":
    print("result",a - b)
    
elif choice == "*":
    print("result",a*b)
    
elif choice =="/":
    if b != 0:
        print("result",a/b)
    else: print("error,solution not defined")
