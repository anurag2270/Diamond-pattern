def diamondpattern(n):
    for i in range(1,n+1):
        for spaces in range(1,(n-i)+1):
            print(" ",end="")
        for stars in range(1,(2*i-1)+1):
            print("*",end="")
        print("\n")
n = int(input())
diamondpattern(n)

