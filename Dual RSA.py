#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import random


# In[2]:


def isprime(no):
    for n in range(2, no): 
        if (no % n) == 0:
            break
        else:
            return True
    return False


# In[3]:


def get_nos(ne,n):
    
    no=int((n/2)-ne)
    list1=list(range(2**(ne-1),(2**(ne))))
    list2=list(range(2**(no-1),(2**(no))))
    
    x1 = random.choice(list1)
    
    x2 = random.choice(list2)
    
    
    p1=x1*x2 + 1
    
    
        
    #print('x1 and x2 are',x1,x2)
    list1new=list1.copy()
    list2new=list2.copy()

    while(isprime(p1)!=True):
        list2new=list2.copy()
        while(isprime(p1)!=True):
            list2new.remove(x2)
            if (len(list2new)==0):
                #print('p1 is',p1) 
                break
            x2= random.choice(list2new)
            p1=x1*x2 + 1    
        list1new.remove(x1)
        if (len(list1new)==0):
                print('p1 is',p1) 
                break
        x1= random.choice(list1new)
        p1=x1*x2 + 1

        
    #print('y2 is',y2)
    list2new=list2.copy()
    list2new.remove(x2)
    y2= random.choice(list2new)
    p2=x1*y2 + 1
    while((isprime(p2)!=True)&(p1==p2)):
        list2new.remove(y2)
        if (len(list2new)==0):
            #print('p2 is',p2)
            break
        y2= random.choice(list2new)
        p2=x1*y2 + 1  

        
    #print('y1 is',y1)
    list1new=list1.copy()
    list1new.remove(x1)
    y1= random.choice(list1new)
    q1 = y1*y2 + 1
    while((isprime(q1)!=True)&(p2==q1)&(p1==q1)):
        list1new.remove(y1)
        if (len(list1new)==0):
            #print('q1 is',q1)
            break
        y1= random.choice(list1new)
        q1 = y1*y2 + 1
    
    return p1,q1,p2,x1,x2,y1,y2
  


# In[4]:


def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


# In[5]:


def multiplicative_inverse(e, phi):
    i=1
    d=1/e
    while(d!=int(d)):
        d=((phi*i)+1)/e
        i=i+1
    return int(d)


# In[61]:


def generate_keypair(ne,n,p1,q1,p2,x1,x2,y1,y2):
    prod=x1*x2*y1*y2
    list1=list(range(2**(ne-1),(2**(ne))))
    e=random.choice(list1)
    #print('e is',e)
    phi1=(p1-1)*(q1-1)
    g=gcd(e, prod)
    q2=0
    n1=p1*q1
    n2=0
    while(isprime(int(q2))!=True):
        #print('q2 is not prime \n\n\n\n')
        while (g!=1):
            list1.remove(e)
            #print('e removed')
            if (len(list1)==0):
                p1,q1,p2,x1,x2,y1,y2=get_nos(ne,n)
                list1=list(range(2**(ne-1),(2**(ne))))
            e=random.choice(list1)
            g=gcd(e, prod)
        d=multiplicative_inverse(e, phi1)
        k1=(e*d-1)/phi1
        q2 = k1*x2 + 1
        n2=p2*q2
        #print('q2 is',q2)
        if (len(list1)==0):
            print('problem, repeat get_nos')
            break
    
    
    return ((e, n1,int(n2)),(d,n1,int(n2)))


# In[64]:


print("RSA Encryption/Decryption")
p1,q1,p2,x1,x2,y1,y2=get_nos(ne=3,n=15)
print("Generating your public/private keypairs now . . .")
public,private = generate_keypair(3,15,p1,q1,p2,x1,x2,y1,y2)
print("Your public key is ", public ," and your private key is ", private)


# In[ ]:



