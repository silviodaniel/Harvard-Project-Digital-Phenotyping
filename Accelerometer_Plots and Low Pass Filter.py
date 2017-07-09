# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 00:08:32 2017

@author: Silvio
"""
import os
os.getcwd()
os.chdir("C:/Users/Silvio/Documents/Python")
#-------------------------------------------------------------------------------
 #Scatter plot of binary data, ie discretized values of variance assigned to 1's and 2's
import pandas as pd
import glob
import matplotlib.pyplot as plt

#Discretized Variance for Silvio's Data
dvariance=[]
sleep_var=[]
silvio_list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/*.csv')
for file in silvio_list_of_files:
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
    elif var>=.003:
        var=1
    dvariance.append(var)
  
#Discretized Variance for Rey's Data
len(rey_dvariance)
rey_dvariance=[]
sleep_var=[]
count=0#59 files
rey_list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/o6bokidk/accelerometer/*.csv')
for file in rey_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))#St deviation
    if var<.15:
        var=0
        #sleep_var.append(var)
    elif var>=.15:
        var=1
        #sleep_var.append(var)
    rey_dvariance.append(var)    #This will return values of t for the tick marks, looping over 24 hours
    count+=1


#start on June 20th,3PM
#must code to put in null values for in between

len(silvio_t)
#59 hours

silvio_full=[]
for hour in silvio_t:
    if silvio_t[hour]==silvio_t[hour]:
        
    elif silvio_t[hour+1]!=silvio_t[hour]+1:
        #if next value not consecutive
        silvio_full=silvio_t.append(hour+1)

#create a function that takes hours from start date to end date



        
dic_silvio={}
for hour in range(n):
    if 
    dic_silvio={#dictionary with hours as keys, and variance, rawvariance, 
            #day, daily hour as tuple and values
        hour:(0,.009,0,13),	#tuples
        1:null,
        2:null,
        
        dic_silvio[hour]=(dvariance,variance,day,daily_hour,week)

#TO GET TICK MARKS AND SAVE DATE & TIMES
import re

silvio_datetime=[]
for file in silvio_list_of_files:
    date_time=re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    print(date_time)
    silvio_datetime.append(date_time)

silvio_t=[]
for t in silvio_datetime:
    splitted=t.split()
    time=splitted[1]
    silvio_time=time[:2]
    silvio_time=int(silvio_time)
    silvio_t.append(silvio_time)

#Rey's
rey_datetime=[]
for file in rey_list_of_files:
    date_time=re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    print(date_time)
    rey_datetime.append(date_time)
    
rey_t=[]
for t in silvio_datetime:
    splitted=t.split()
    time=splitted[1]
    rey_time=time[:2]
    rey_time=int(rey_time)
    rey_t.append(rey_time)

len(rey_t)
for v in range(len(Time_of_sleep)):
    if Time_of_sleep[v] == Time_of_sleep[0]:#at first point, if next value is consecutive..
        if v==0:
            if Time_of_sleep[v]==Time_of_sleep[v+1]-1:
                print("Went to sleep at " + str(Time_of_sleep[v]))#sleep!
                print("A")
    elif Time_of_sleep[v] == Time_of_sleep[-1]:#if at last position,
        if v==33:#then print woke up
               print("Woke up at " + str(Time_of_sleep[v]))
               print("B")        
    elif Time_of_sleep[v-1] != Time_of_sleep[v]-1 and Time_of_sleep[v+1] == Time_of_sleep[v]+1:
        print("Went to sleep at " + str(Time_of_sleep[v]))
        print("C")
    elif Time_of_sleep[v-1] ==Time_of_sleep[v]-1 and Time_of_sleep[v+1] != Time_of_sleep[v]+1:
        print("Woke up at " + str(Time_of_sleep[v]))
        print("D")
        
def mod(a,b):
    return a%b    
silvio_t=[3]
for i in silvio_t:
    if len(silvio_t)<len(silvio_times):#from dictionary, need to cut!
        silvio_t.append(mod(i+1,24))
    else:
        exit
    
len(rey_dvariance)
rey_t=[15]
for i in rey_t:
    if len(rey_t)<len(rey_times):#
        rey_t.append(mod(i+1,24))
    else:
        exit
  
      
#Plot of Phone Accelerometer Variance Discretized to 1's and 0's, no filter applied
#SILVIO
length = list(range(0,len(silvio_times)))#
plt.plot(length,silvio_times[],"ko",linewidth=2,markersize=1);
plt.title("Variance of Silvio's Phone Accelerometer",fontsize=15)
plt.xlabel('Time (Hours) Since Day 1',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.xticks(length[::10],silvio_t[::10])
plt.savefig("Silvio's Variance_No Filter.pdf")

#REY
length = list(range(0,len(r_dvariance)))#
plt.plot(length,r_dvariance,"ko",linewidth=2,markersize=1);
plt.title("Variance of Rey's Phone Accelerometer",fontsize=15)
plt.xlabel('Time (Hours) Since Day 1',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.xticks(length[::10],rey_t[::10])

###############################################################
#?plt.xticks
#LOW PASS FILTER

lpf_var=dvariance
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
#want 7 rows, 24 columns
#do we want 3 rows on each day for each of us??
#how can I add in data to also go on this heat map from more files?

#1's are white (activity), 0's are black (sleep)
#begins bottom left, goes right and up
#all days, with 8 hours
rey_data      = [int(random.random()>0.5) for i in range(n)]
danielle_data = [int(random.random()>0.5) for i in range(n)]
silvio_data   = [int(random.random()>0.5) for i in range(n)]

Index= ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
Cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
#Making data dvariance into an array that fits the heat map, 7 by 24
#USE the dvariance calculated from before code
dvariances=dvariance+[0,0,0,0,0]#just adding 5 more rows (5 zeros) in order to fit the dimensions 
#of the heat map
dvariance1=np.array(dvariances)
dat=dvariance1.reshape((7,24))

#RUN FROM HERE, if you want to run again
df = DataFrame(dat, index=Index, columns=Cols)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.pcolor(df,cmap='inferno')
plt.title('Activity Levels: Variance of Phone Accelerometer',fontsize=14)
plt.xlabel('Time (Hours)',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.savefig("Variance Heat Map_No Filter.pdf")


#PLAYING WITH HEAT MAP BELOW
Index= ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
Cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
#Making data dvariance into an array that fits the heat map, 7 by 24
#USE the dvariance calculated from before code
#
df = DataFrame(abs(np.random.randn(7,24)), index=Index, columns=Cols)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.pcolor(df,cmap='inferno')
plt.title('Activity Levels: Variance of Phone Accelerometer',fontsize=14)
plt.xlabel('Time (Hours)',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)

plt.savefig("Heat Map_Random Data2.pdf")

Index= list(range(1,24))#, 'ddd', 'eee','fff','ggg','hhh',9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
Cols = list(range(1,15))#, 'D','E','F']
#Index= ['I ', 'want ', 'to ', 'change', 'this']
#Cols = ['A', 'B', 'C', 'D']
#data= abs(np.random.randn(5,4))
#24 by 15 below
data=np.array([[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0,1,1,1,1,1],])
df = DataFrame(data, index=Index, columns=Cols)
#fig,ax=plt.subplots()
#plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
#plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
rlabels=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
clabels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
ax.set_xticklabels(rlabels, minor=False)
ax.set_yticklabels(clabels, minor=False)
#plt.pcolor(df,cmap=plt.cm.Blues)#will change to different blue shades
plt.pcolor(df,cmap='inferno')
plt.title('Variance of Phone Accelerometer',fontsize=15)
plt.xlabel('Time (Hours)',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.show()

cmap = colors.ListedColormap(['green','red','blue','black','white'])
plt.pcolor(df,cmap=cmap) 

plt.pcolor(df,edgecolors='k',linewidths=4)#blue, green, yellow shades
plt.pcolor(df,rgb/255.0)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()

#testing
fig,ax=plt.subplots()
fig.canvas.draw()
labels=[item.get_text() for item in ax.get_xticklabels()]
labels[1]='Testing'

ax.set_xticklabels(labels)
plt.show()

Index= ['I ', 'want ', 'to ', 'change', 'this']
Cols = ['A', 'B', 'C', 'D']
df = DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)

plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()

import heatmap
import random

hm = heatmap.Heatmap()
pts = [(random.uniform(-77.012, -77.050), random.uniform(38.888, 38.910)) for x in range(100)]
hm.heatmap(pts)

##
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'])
data=[trace]
py.iplot(data, filename='labelled-heatmap')

import numpy as np 
from pandas import *
import matplotlib.pyplot as plt
from matplotlib import colors

#RGB?
#Example: suppose you want red to increase from 0 to 1 over the bottom half, 
#green to do the same over the middle half, and blue over the top half. 
#Then you would use:
cdict = {'red':   [(0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)],

         'green': [(0.0,  0.0, 0.0),
                   (0.25, 0.0, 0.0),
                   (0.75, 1.0, 1.0),
                   (1.0,  1.0, 1.0)],

         'blue':  [(0.0,  0.0, 0.0),
                   (0.5,  0.0, 0.0),
                   (1.0,  1.0, 1.0)]}
 pip install plotly 

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


