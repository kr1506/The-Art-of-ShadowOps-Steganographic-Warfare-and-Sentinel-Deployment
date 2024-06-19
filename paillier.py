import random
def gcd_eu(a,b):
    if(a==0):
        return b
    return gcd_eu(b%a,a)

def not_equal(p,q):
    if(p==q):
        q=random.randint(0,200)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

p=random.randint(0,200)
q=random.randint(0,200)
while (is_prime(p)==False or is_prime(q)==False):
    p=random.randint(0,200)
    q=random.randint(0,200)
    not_equal(p,q)

n=p*q
phi=(p-1)*(q-1)
g=n+1
e=2

while(e<n):
    if(gcd_eu(e,n)==1):
        break
    e+=1 

def mod_inverse(e, phi):
    phi0, x0, x1 = phi, 0, 1  
    while e > 1:
        q = e // phi        
        phi, e = e % phi, phi  
        x0, x1 = x1 - q * x0, x0
    return x1 + phi0 if x1 < 0 else x1  

msg=int(input("Enter message:"))
encrypted_message=((pow(g,msg))*(pow(e,n)))%(pow(n,2))
print(encrypted_message)

