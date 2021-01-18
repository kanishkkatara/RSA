import random
import time

def PrimeList(start,end): 
    primes = [];
    for val in range(start, end + 1): 
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: 
                    break
            else:
                primes.append(val)
    return primes

def get_nos(start,end):
    primes=PrimeList(start,end)
    p = random.choice(primes)
    primes.remove(p)
    q= random.choice(primes)
    return p,q

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def multiplicative_inverse(e, phi):
    i=1
    d=1/e
    while(d!=int(d)):
        d=((phi*i)+1)/e
        i=i+1
    return int(d)

def generate_keypair(p, q):
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randrange(1, phi)
    g=gcd(e, phi)
    while g!=1:
        e=random.randrange(1, phi)
        g=gcd(e, phi)
    d=multiplicative_inverse(e, phi)
    return ((e, n),(d, p,q))

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
    #key, n = pk(d,n)
    plain=[]
    d,p,q= pk
    dp=d%(p-1)
    dq=d%(q-1)
    for t in ciphertext: 
        Cp=(t**dp)%p
        Cq=(t**dq)%q
        m0=((Cp-Cq)**(p-1))%d
        plain.append(chr(Cp+(m0*p)))
        
    return ''.join(plain)

print("RSA Encryption/Decryption - CRT Decryption")
p,q=get_nos(37,1000)
print('p = ', p, ', q = ', q)
print("Generating your public/private keypairs now . . .")
public, private = generate_keypair(p, q)
print("Your public key is ", public ," and your private key is ", private)
message = input("Enter a message to encrypt: ")
encrypted_msg = encryption(public, message)
print("Your encrypted message is: ")
print(''.join(map(lambda x: str(x), encrypted_msg)))
print("Decrypting message . . .")
print("Your message after decryption is:", decryption(private, encrypted_msg))
