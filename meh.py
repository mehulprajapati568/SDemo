a=input("enter a: ")  #value of first num
b=input("enter b: ")  #value of second num
c=input("enter c: ")  #value of third num
d=input("enter d: ")  #value of fourth num
print a+b+c+d         #add of 4 num
print a+b  #add of first 2 num
print c+d  #add of second 2 num
print (a+b)/(c+d)

if a>1 and a<14:
        ad=a+b+c+d
        print ("addition=",ad)
        if a==13:
            print("invalid")
elif a>15 and a<30:
            sb=a-b-c-d
            print ("subtraction=",sb)
            if a==29:
                print("invalid")
else:
                dd=a/b/c/d
                print ("division=",dd)
                
