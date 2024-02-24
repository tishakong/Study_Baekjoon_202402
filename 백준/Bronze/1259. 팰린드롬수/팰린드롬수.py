while True:
    A=input()
    if A=="0":
        break
    else:
        reverseA = A[::-1]
        if A == reverseA:
            print("yes")
        else:
            print("no")
                
                
