#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code

def testAll():
    assert (message([1]) == [0, 0, 1, 1])
    assert (message([0, 0, 1]) == [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])
    assert (message([0, 1, 1, 0]) == [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0])
    assert (message([1, 1, 1, 1, 0, 1]) == [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0])
    assert (message([]) == [])


    assert (hammingEncoder([1, 1, 1]) == [])
    assert (hammingEncoder([1, 0, 0, 0]) == [1, 1, 1, 0, 0, 0, 0])
    assert (hammingEncoder([0]) == [0, 0, 0])
    assert (hammingEncoder([0, 0, 0]) == [])
    assert (hammingEncoder([0, 0, 0, 0, 0, 0]) == [])
    assert (hammingEncoder([0, 0, 1, 1]) == [1,0,0,0,0,1,1])
    assert (hammingEncoder([1,1,0,1,0,0,1,1,0,1,1]) == [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1])
    assert (hammingEncoder([1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1]) == [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1])
    assert (hammingEncoder([]) == [])

    
    assert (hammingDecoder([1, 0, 1, 1]) == [])
    assert (hammingDecoder([0, 1, 1, 0, 0, 0, 0]) == [1, 1, 1, 0, 0, 0, 0])
    assert (hammingDecoder([1, 0, 0, 0, 0, 0, 1]) == [1, 0, 0, 0, 0, 1, 1])
    assert (hammingDecoder([1, 1, 0]) == [1, 1, 1])
    assert (hammingDecoder([1, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0])
    assert (hammingDecoder([1,0,1,1,1,0,1]) == [1, 0, 1, 0, 1, 0, 1])
    assert (hammingDecoder([]) == [])

    

    assert (messageFromCodeword([1, 0, 1, 1]) == [])
    assert (messageFromCodeword([1, 1, 1, 0, 0, 0, 0]) == [1, 0, 0, 0])
    assert (messageFromCodeword([1, 0, 0, 0, 0, 1, 1]) == [0, 0, 1, 1])
    assert (messageFromCodeword([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1])
    assert (messageFromCodeword([0, 0, 0, 0]) == [])
    assert (messageFromCodeword([]) == [])


    

    assert (dataFromMessage([1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == [])
    assert (dataFromMessage([1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == [])
    assert (dataFromMessage([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == [0, 1, 1, 0, 1])
    assert (dataFromMessage([0, 0, 1, 1]) == [1])
    assert (dataFromMessage([0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]) == [0, 0, 1])
    assert (dataFromMessage([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]) == [0, 1, 1, 0])
    assert (dataFromMessage([0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]) == [1, 1, 1, 1, 0, 1])
    assert (dataFromMessage([1, 1, 1, 1]) == [])
    assert (dataFromMessage([]) == [])
    

    assert (repetitionEncoder([0], 4) == [0, 0, 0, 0])
    assert (repetitionEncoder([0], 2) == [0, 0])
    assert (repetitionEncoder([1], 4) == [1, 1, 1, 1])
    assert (repetitionEncoder([1], 0) == [])
    assert (repetitionEncoder([1,1], 2) == [])
    assert (repetitionEncoder([2], 2) == [])
    assert (repetitionEncoder([1], -2) == [])
    assert (repetitionEncoder([1], 2.32) == [])
    assert (repetitionEncoder([1], 0.32) == [])
    assert (repetitionEncoder([],2) == [])
    

    assert (repetitionDecoder([1, 1, 0, 0]) == [])
    assert (repetitionDecoder([1, 0, 0, 0]) == [0])
    assert (repetitionDecoder([0, 0, 1]) == [0])
    assert (repetitionDecoder([1, 1, 1, 1]) == [1])
    assert (repetitionDecoder([]) == [])

    print('all tests passed')
    
import random, math
import numpy as np
def randomflip(data):
    bit = random.randrange(len(data))
    data[bit] = (data[bit]+1)%2
    return data

def testdata(inp, fliprandombit=False):
    if not fliprandombit:
        assert (inp == dataFromMessage(messageFromCodeword(hammingDecoder(hammingEncoder(message(inp))))))
    else:
        assert (inp == dataFromMessage(messageFromCodeword(hammingDecoder(randomflip(hammingEncoder(message(inp)))))))


def test_up_to(n, randflip=False, step=1):
    for i in range(1,n, step):
        testdata(decimalToVector(i,math.ceil(math.log2(i))), randflip)
    print("all tests passed")



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
    if len(p)==0:
        return False
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
    if valid_inp(m):
        power=r-1
        decimal=0
        for s in range(r):
            decimal+=(2**power)*m[s]
            power-=1
        return decimal
    else:
        return []

def message(a):
    if valid_inp(a):
        m=[]
        r=2
        k=2**r-r-1
        while k-r<len(a):
            r+=1
            k=2**r-r-1        
        len_bin=decimalToVector(len(a),r)
        m.extend(len_bin)
        m.extend(a)
        for i in range(r+len(a),k):
            m.append(0)
        return m
    else:
        return []


def MULT(m,G,colG):    
    sum1=0
    col=[]
    r=2
    k=2**r-r-1
    while k!=len(m):
        r+=1
        k=2**r-r-1
    result=[]    
    for j in range(colG):
        sum1=0
        col.clear()
        col = [item[j] for item in G]        
        for i in range(len(m)):
            sum1+=m[i]*col[i]
           
        result.append(sum1%2)
    return result
    
def hammingEncoder(m):
    result_l=[]
    if valid_inp(m):
        r=2
        k=2**r-r-1
        while k!=len(m):
            r+=1
            k=2**r-r-1
            if k>len(m):
                return []
        count=0
        G=np.array(hammingGeneratorMatrix(r),dtype=int)
        sizeG=G.size
        rowsG=len(G)
        if rowsG !=len(m):
            return []
        colG=sizeG//rowsG
        result1= MULT(m,G,colG)
        for k in result1:           
            result_l.append(k)
        return result_l
    else:
        return []


def dataFromMessage(m):
    if valid_inp(m):
        lengthL=[]
        output=[]
        length=0
        r=2
        k=2**r-r-1
        while k!=len(m):
            r+=1
            k=2**r-r-1
            if k>len(m):
                return []
        for i in range(r):
            lengthL.append(m[i])    
        length=VectorTodecimal(lengthL,len(lengthL))
        if length==0:
            return []
        if len(m)-r<length:
            return []
        for j in range(r,r+length):
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
    if valid_inp(v):
        r=2
        k=2**r-1
        while(k!=len(v)):
            r+=1
            k=2**r-1
            if k>len(v):
                return []
        H_= np.array(GenerateH(r),dtype=int)
        if len(v)!=len(H_):
            return []
        pos_cha_bin=VectorMulMet(v,H_)        
        pos_chan_den=VectorTodecimal(pos_cha_bin,r)
        if pos_chan_den>len(v):
            return []            
        if v[pos_chan_den-1]==0:
            v[pos_chan_den-1]=1
        else:
             v[pos_chan_den-1]=0
        return v
    else:
        return []



def messageFromCodeword(c):
    if valid_inp(c):
        power=0
        r=2
        k=2**r-1
        while k!=len(c):
            r+=1
            k=2**r-1        
            if k>len(c):
                return []
        j=1
        for i in range(2**(r-1)+1):
            if i==2**power:
                power+=1
                del c[i-j]
                j+=1
        return c
    else:
        return []

 
def repetitionEncoder(m,n):
    if type(n) != int:
        return []
    if valid_inp(m) and n>0 and len(m)==1:
        new_list=[]
        for i in range (0,n):
            new_list.extend(m)
        return new_list
    else:
        return []

def repetitionDecoder(v):
    if valid_inp(v) and len(v)>0:
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



print(testAll())
