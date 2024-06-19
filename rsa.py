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
e=random.randint(1,200)

while(e<phi):
    if(gcd_eu(e,phi)==1):
        break
    e+=1                   #this is to see if the e that we selected at once is not a factor of n

def mod_inverse(e, phi):
    phi0, x0, x1 = phi, 0, 1  # Initializing variables
    while e > 1:
        q = e // phi           # Compute the quotient
        phi, e = e % phi, phi  # Update phi and e
        x0, x1 = x1 - q * x0, x0  # Update x0 and x1
    return x1 + phi0 if x1 < 0 else x1  # Ensure the result is positive
d=mod_inverse(e,phi)

message=int(input("Enter message to encrypt:"))
encrypted_message=(pow(message,e))%(n)
print(encrypted_message)

