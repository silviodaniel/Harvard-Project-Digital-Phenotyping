# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 00:08:32 2017

@author: Silvio
"""

os.getcwd()
os.chdir("C:/Users/Silvio/Documents/Python")
#-------------------------------------------------------------------------------
 #Scatter plot of binary data, ie discretized values of variance assigned to 1's and 2's
import pandas as pd
import glob
import matplotlib.pyplot as plt

dvariance=[]
sleep_var=[]
t=[3,4,5]
list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/*.csv')
for file in list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=sum(df.var(axis=0))
    sumofsq=sum(x**2)+sum(y**2)+sum(z**2)
    if var<.003:
        var=0
        sleep_var.append(var)
    elif var>=.003:
        var=1
        sleep_var.append(var)
    dvariance.append(var)
    
    #This will return values of t for the tick marks, looping over 24 hours
def mod(a,b):
    return a%b    
t=[3]
for i in t:
    if len(t)<len(dvariance):
        t.append(mod(i+1,24))
    else:
        exit
        
#Plot of Phone Accelerometer Variance Discretized to 1's and 0's, no filter applied
length = list(range(0,len(dvariance)))#
plt.plot(length,dvariance,"ko",linewidth=2,markersize=1);
plt.title('Variance of Phone Accelerometer',fontsize=15)
plt.xlabel('Time (Hours) Since Day 1',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.xticks(length[::10],t[::10])

#ISSUE: should output all the times during which variance was less than threshold, indicating
#values when asleep
Time_of_sleep=[]
for i in dvariance:
    if i<.003:
        Time_of_sleep.append(t[dvariance.index(i)])

###############################################################
#?plt.xticks
#LOW PASS FILTER

check=[]#****this is to check which if and else statements run: the letter that prints
#shows me if this condition was run in the for loop
for i in lpf_var:#for i in low pass filter of variance
    if lpf_var.index(i)==0:#at position zero
        x=lpf_var[i+1]+lpf_var[i+2]#sum the iterations to the right, 2 of them
        if x>2:#checking if sum >2, because during this time (around 3am) there was sleep
            lpf_var[i]=1#iteration will be changed to 1
            check.append("A")#
        else:
            lpf_var[i]=0
            check.append("B")
    elif lpf_var.index(i)==1:#at position 1, 
        x=lpf_var[i+1]+lpf_var[i+2]+lpf_var[i-1]
        if x>2:
            lpf_var[i]=1#iteration will be changed to 1
            check.append("C")
        else:
            lpf_var[i]=0
            check.append("D")
    elif lpf_var.index(i)==len(lpf_var)-1:
        x=lpf_var[i-1]+lpf_var[i-2]
        if x>1:
            lpf_var[i]=1#iteration will be changed to 1
            check.append("E")
        else:
            lpf_var[i]=0
            check.append("F")
    elif lpf_var.index(i)==len(lpf_var)-2:
        x=lpf_var[i-1]+lpf_var[i-2]+lpf_var[i+1]
        if x>1:
            lpf_var[i]=1#iteration will be changed to 1
            check.append("G")
        else:
            lpf_var[i]=0
            check.append("H")
    else:
        x=lpf_var[i-1]+lpf_var[i-2]+lpf_var[i+1]+lpf_var[i+2]
        if x>2:
            lpf_var[i]=1#iteration will be changed to 1
            check.append("I")
        else:
            lpf_var[i]=0
            check.append("J")
len(check)#checking which statemetns ran

#Plot for NO FILTER APPLIED
length = list(range(0,len(dvariance)))#
plt.plot(length,dvariance,"ko",linewidth=2,markersize=1);
plt.title('Variance of Phone Accelerometer',fontsize=15)
plt.xlabel('Time (Hours) Since Day 1',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.xticks(length[::10],t[::10])
plt.savefig("Variance of Phone Accelerometer.pdf")

#PLOT FOR LOW PASS FILTER
length = list(range(0,len(lpf_var)))#
plt.plot(length,lpf_var,"ko",linewidth=2,markersize=1);
plt.title('Variance with Low Pass Filter',fontsize=15)
plt.xlabel('Time (Hours) Since Day 1',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.xticks(length[::10],t[::10])
plt.savefig("Variance Low Pass Filter2.pdf")
        
#######
#HEAT MAP
import heatmap
import random

hm = heatmap.Heatmap()
pts = [(random.uniform(-77.012, -77.050), random.uniform(38.888, 38.910)) for x in range(100)]
hm.heatmap(pts)


import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])
data=[trace]
py.iplot(data, filename='labelled-heatmap')


##NOTES--------------------------------------------------------------------------
    
random=[1,1,0,0,1,2]
random.index(1)#where =1, specifies location of index
random.index(2)==len(random)-1
len(random)-1

for i in random:
    if random.index(i)==-1:
        print(random.index(i))
print(a)
dvariance
sum(random)
import numpy as np
np.sum(random[1],random[2])

lpf_var=dvariance
lpf_var.index(0)==1
lpf_var = np.array((lpf_var))
lpf_var[1]+lpf_var[2]
type
np.sum(lpf_var[1],lpf_var[2])

c=[] #Scatter plot of general data
t=[15] 
list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/*.csv')
for file in list_of_files:
    columns = ['timestamp', 'UTCtime', 'Accuracy','x', 'y', 'z']
    data=pd.read_csv(file,header=0, sep= ',', names = columns)
    data.drop(data.columns[[0,1,2]], axis=1, inplace = True)
    x=data['x'].values
    y=data['y'].values
    z=data['z'].values
    t1 = np.var(x)
    t2 = np.var(y)
    t3 = np.var(z)
    x=t1 + t2 + t3
    #if x<.15:
        #x=0
        #c.append(x)
    #if x>=.15:
        #x=1
    c.append(x)
    
def mod(a,b):
    return a%b
    
mod(2,3)

t=[3]
for i in t:
    if len(t)<len(dvariance):
        t.append(mod(i+1,24))
    else:
        exit
t

x = list(range(0,len(c)))
x
plt.plot(x,c,'ob')
plt.xticks(x[::3],t[::3])

lpf_var=dvariance
for point in lpf_var:
    #if point's neighbors, specified by range n (2), to the left
    #or to the right add up to at least n, then change variance value
    #to 1; otherwise, leave at zero
    r=2
    neighbor_count=[]
    count=[]
    #? create for loop : for neighbor in range(0,point): if...else....
    for neighbor in range(lpf_var[point-2],lpf_var[point+2]):
        if neighbor==1:
            neighbor_count.append(1)
    #if lpf_var[point] ==lpf_var[point+2]-2 :
 #if the dvariance has n range points to the right, then sum all values ==1
 #if dvariance has n range points to the left, then sum all values==1
 #else, meaning at edges and no points to left/right, do nothing
        #how to code if a value exists in a range????????
        lpf_var=1
        elif lpf_var:
     #??Issue: where to put sum in for each range of values of 1 
        #if the sum of the set of neighbors for 1 point is >2, then change lpf_var to 0/1
        lpf_var

def neighbors(r,value):
    return list(range(value-r,value+r+1))

def neighbors(r,value):
    return i(range(value-r,value+r+1))
neighbors(2,4)

for point in lpf_var:
    #if point's neighbors, specified by range n (2), to the left
    #or to the right add up to at least n, then change variance value
    #to 1; otherwise, leave at zero
    #for each point, if sum of neighbors(defined as range before)>2
    neighbors=range(lpf_var[point-2],lpf_var[point+2])
    r=2
    neighbor_count=[]
    count=[]
    #? create for loop : for neighbor in range(0,point): if...else....
    for neighbor in neighbors:
        if neighbor==1:
            neighbor_count.append(1)
    #if lpf_var[point] ==lpf_var[point+2]-2 :
 #if the dvariance has n range points to the right, then sum all values ==1
 #if dvariance has n range points to the left, then sum all values==1
 #else, meaning at edges and no points to left/right, do nothing
        #how to code if a value exists in a range????????
        lpf_var=1
        elif lpf_var:


