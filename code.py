
print('welcome to python calculator')
def val():
    a = int(input("Enter your number: "))
    print('''+   -   /   *   %   |   //''')
    b = input("Choose the operator: ")
    c = int(input("Enter other number: "))
    return a,b,c

def optr(a,b,c):
    if b=='+':
        return (a+c)
    elif b=='-':
        return (a-c)
    elif b=='/':
        return (a/c)
    elif b=='*':
        return (a*c)
    elif b=='%':
        return (a%c)
    elif b=='//':
        return (a//c)
    else:
        return ("enter valid operator!")
    
while True:
    a,b,c = val()
    print(optr(a,b,c))
    f = optr(a,b,c)

    d = input(f"If you want to continue press 'y', want start new calculation press 'n', exit press 'q': ")
    while d == 'Y' or d=='y':
        a = f
        print('''+   -   /   *   %   |   //''')
        b = input("Choose the operator: ")
        c = int(input("Enter other number: "))
        print(optr(a,b,c))
        d = input(f"If you want to continue press 'y', want start new calculation press 'n', exit press 'q': ")
        f = optr(a,b,c)
    if d == 'N' or d == 'n':
        pass
    elif d == 'q':
        break
    else:
        print("Error")
        break

print('Thank you')
