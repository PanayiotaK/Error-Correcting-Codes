#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
import numpy as np
def hammingGeneratorMatrix(r):
    n = 2**r-1
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)
    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))
    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G


#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n

def valid_inp(p):
    for i in range(len(p)):
        if p[i]!=0 and p[i]!=1:
            return False
    else:
        return True

def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v

def VectorTodecimal(m,r):
    if(valid_inp(m)==True):
        power=r-1
        decimal=0
        for s in range(r):
            decimal+=(2**power)*m[s]
            power-=1
        return decimal
    else:
        return []


def message(a):
    if(valid_inp(a)==True):
        m=[]
        r=2
        k=2**r-r-1
        while(k-r<len(a)):
            r+=1
            k=2**r-r-1
        #print("r ",r, "k",k)
        len_bin=decimalToVector(len(a),r)
        m.extend(len_bin)
        m.extend(a)
        for i in range(r+len(a),k):
            m.append(0)
        return m
    else:
        return []
a=[]
print(message(a))


def hammingEncoder(m):
    if(valid_inp(m)==True):
        r=2
        k=2**r-r-1
        while(k!=len(m)):
            r+=1
            k=2**r-r-1
            if(k>len(m)):
                return []
        G=hammingGeneratorMatrix(r)
        result=np.dot(m,G)
        result1=list(result)
        return result1
    else:
        return []

print(hammingEncoder([1,0,0,0]))      


def dataFromMessage(m):
    if(valid_inp(m)==True):
        lengthL=[]
        output=[]
        length=0
        r=2
        k=2**r-r-1
        while(k!=len(m)):
            r+=1
            k=2**r-r-1
            if(k>len(m)):
                return []
        #print("r: ",r)
        for i in range(r):
            lengthL.append(m[i])    
        length=VectorTodecimal(lengthL,len(lengthL))
        if length==0:
            return []
        if len(m)-r<length:
            #print("len(m)-r<length")
            return []
        #print("length: ",length)
        for j in range(r,r+length):
            #print("J ",j)
            output.append(m[j])
        for k in range(r+length,len(m)):
            if m[k]!=0:            
                return []
        return output
    else:
        return []

def GenerateH(r):
    H=[]
    for i in range(2**r-1):
        H.append(decimalToVector(i+1,r))
    return H



def VectorMulMet(v,H):
    if(valid_inp(v)==True):
        sum1=0
        col=[]
        r=2
        k=2**r-1
        while(k!=len(v)):
            r+=1
            k=2**r-1
        result=[]
        for j in range(r):
            sum1=0
            col.clear()
            col = [item[j] for item in H] 
            for i in range(len(v)):
                sum1+=v[i]*col[i]
            result.append(sum1%2)
        return result
    else:
        return []

def hammingDecoder(v):
    if(valid_inp(v)==True):
        r=2
        k=2**r-1
        while(k!=len(v)):
            r+=1
            k=2**r-1
            if k>len(v):
                return []
        #print("v:" ,v)
        H_= np.array(GenerateH(r),dtype=int)
        #print(H_)
        #print("r ",r)
        pos_cha_bin=VectorMulMet(v,H_)
        #print("mult: ", pos_cha_bin)
        pos_chan_den=VectorTodecimal(pos_cha_bin,r)
        #print("possition: ",pos_chan_den)
        if v[pos_chan_den-1]==0:
            v[pos_chan_den-1]=1
        else:
             v[pos_chan_den-1]=0
        return v
    else:
        return []



def messageFromCodeword(c):
    if(valid_inp(c)==True):
        power=0
        r=2
        k=2**r-1
        while(k!=len(c)):
            r+=1
            k=2**r-1        
            if k>len(c):
                return []
        
        for i in range(2**r):
            if i==2**power:
                power+=1
                #print("i: ",i)
                del c[i-1]
        return c
    else:
        return []

    
def repetitionEncoder(m,n):
    if(valid_inp(m)==True):
        new_list=[]
        for i in range (0,n):
            new_list.extend(m)
        return new_list
    else:
        return []

def repetitionDecoder(v):
    if(valid_inp(v)==True):
        count1=0
        count0=0
        L=[]
        for i in v:
            if i ==1:
                count1+=1
            else:
                count0+=1
        if count0>count1:
            L.append(0)        
        elif count1>count0:
            L.append(1)
        return L
    return []



    
