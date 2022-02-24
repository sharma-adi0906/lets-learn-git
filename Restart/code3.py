m = (input("Enter the number: "))

a = len(m)

if a%2 == 0:
    
    d = a//2


    b = a - d

    p = m[0:b] 
    q = m[b:a]

    print(p)
    print(q)
    
    x = int(p)
    y = int(q)

    if  x > y :
        print("magical number")
    else:
        print("Normal number")

else: 
    d = a//2

    b = a-d
    
    p = m[0:b-1]
    q = m[b:a]
    
    x = int(p) 
    y = int(q)

    if x > y:
        print("magical number")
    else:
        print("Normal number")
