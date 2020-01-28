# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:56:52 2020

@author: Jayant malhotra

count_row = df.shape[0]  # gives number of row count
count_col = df.shape[1]  # gives number of col count
"""

#   topsis.py data.csv "0.25,0.25,0.25,0.25" "-,+,+,+"
import math
import pandas as pd
import numpy as np
import scipy.stats as ss
import sys

def topsis(a,w,impact):
    
    w=list(w.split(","))
  
    impact=list(impact.split(","))
    df=pd.read_csv(a)
    data=pd.DataFrame(df)
    df=df.astype('float')
    m=[]
    n=[]
    for i in range(0,df.shape[1]):
        column=df.iloc[:,i]
        column = [ x/np.sqrt(sum(np.square(column))) for x in column ]
        column = [ x*float(w[i]) for x in column]
        df.iloc[:,i]=column
        if impact[i]=='+':
            m.append(df.iloc[:,i].max(axis=0))
            n.append(df.iloc[:,i].min(axis=0))
        else:
            n.append(df.iloc[:,i].max(axis=0))
            m.append(df.iloc[:,i].min(axis=0))
    
    S1=[]
    S2=[]     
    for i in range(0,df.shape[0]):
        c=df.iloc[i,:]
        s1=0
        s2=0
        for j in range(0,df.shape[1]):
            s1=s1+(c[j]-m[j])**2
            s2=s2+(c[j]-n[j])**2
        s1=math.sqrt(s1)
        s2=math.sqrt(s2)
        S1.append(s1)
        S2.append(s2)
   
    S3 = [sum(i) for i in zip(S1,S2)] 
    for i in range(0,df.shape[0]):
        if S3[i]==0:
            return print("invalid data")
        
    r = [i/j for i,j in zip(S2,S3)]
    abc=ss.rankdata(r)
    rank=[ abs(i-df.shape[0]-1) for i in abc]
    data['rank']=rank
    return print(data)

if __name__ == "__main__":
    topsis(sys.argv[1],sys.argv[2],sys.argv[3])
        

    


    