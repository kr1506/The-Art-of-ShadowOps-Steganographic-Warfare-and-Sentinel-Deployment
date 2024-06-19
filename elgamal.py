import random

def not_equal(p,q):
    if(p==q):
        q=random.randint(1,p-1)

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
while (is_prime(p)==False):
    p=random.randint(0,200)

def mod_inverse(e, phi):
    phi0, x0, x1 = phi, 0, 1  # Initializing variables
    while e > 1:
        q = e // phi           # Compute the quotient
        phi, e = e % phi, phi  # Update phi and e
        x0, x1 = x1 - q * x0, x0  # Update x0 and x1
    return x1 + phi0 if x1 < 0 else x1  # Ensure the result is positive

a=1
for i in range(1,p):
    for j in range(1,p):
        if ((pow(a,i))%p==(pow(a,j))%p):
            a=i
        else :
            a+=1

#we get "a" which is the primitive root
h=random.randint(0,p)
b=(pow(a,h))%p
print("public key:",p,a,b)
k=random.randint(1,p-1)
msg=int(input("enter message:"))
encrypted_message_1=pow(a,k)%p
encrypted_message_2=(msg*(pow(b,k)))%p
print(encrypted_message_1,encrypted_message_2)