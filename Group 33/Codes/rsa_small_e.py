import random
import time

def get_nos():
    p = random.randrange(1,200)
    q = random.randrange(1,200)
    prime=soe(max(p,q))
    if not (prime[p] and prime[q]):
        p,q=get_nos()
    elif p==q:
        p,q=get_nos()
    elif(p*q<=30):
        p,q=get_nos()
    return p,q

def gcd(a, b):
    while b!=0:
        a,b = b,a%b
    return a

def multiplicative_inverse(e, phi):
    i=1
    d=1/e
    while(d!=int(d)):
        d=((phi*i)+1)/e
        i=i+1
    return int(d)

def soe(n):
    prime=[1 for i in range(n+1)] 
    prime[0]=0
    prime[1]=0
    p=2
    while(p*p<=n): 
        if (prime[p]==1): 
            for i in range(p*2, n+1, p): 
                prime[i]=0
        p+=1
    return(prime)

def generate_keypair(p, q):
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randrange(1, phi)
    g=gcd(e, phi)
    while g!=1:
        e=random.randrange(1, phi)
        g=gcd(e, phi)
    d=multiplicative_inverse(e, phi)
    return ((e, n),(d, n))

def power(b,e,n):
    bi=bin(e)
    x=-1
    ans=1
    t=b%n
    while(bi[x]!='b'):
        if(bi[x]=='1'):
            ans*=t
            ans%=n
        t=(t**2)%n
        x-=1
    return ans

def encryption(pk, plaintext):
    key, n = pk
    cipher = [power(ord(t),key,n) for t in plaintext]
    return cipher

def decryption(pk, ciphertext):
    key, n = pk
    plain = [chr(power(t,key,n)) for t in ciphertext]
    return ''.join(plain)

print("RSA Encryption/Decryption small-e implementation")
p,q=get_nos()
print('p = ', p, ', q = ', q)
print("Generating your public/private keypairs now . . .")
public, private = generate_keypair(p, q)
print("Your public key is ", public ," and your private key is ", private)
message = input("Enter a message to encrypt: ")
encrypted_msg = encryption(private, message)
print("Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
print("Decrypting message . . .")
print("Your message after decryption is: ", decryption(public, encrypted_msg))
