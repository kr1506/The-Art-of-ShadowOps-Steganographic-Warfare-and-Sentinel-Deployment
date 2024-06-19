def gcd_eu(a,b):
    if(a==0):
        return b
    return gcd_eu(b%a,a)

def gcd_o_n(a,b):
    gcd=1
    for i in range(1,(min(a,b)+1)):
        if(a%i==0 and b%i==0):
            gcd=i
    return gcd

a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(gcd_eu(a,b))
print(gcd_o_n(a,b))



