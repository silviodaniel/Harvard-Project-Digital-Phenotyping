# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:04:02 2017

@author: Silvio
"""
import os
os.getcwd()
os.chdir("C:/Users/Silvio/Documents/Python")
import glob
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import random
import re
import datetime
import pandas as pd
#Silvio's Time and Variance
#TASK:
#create a function that takes each list of files and converts to newly named time dictionary
times = {}
silvio_list_of_files = glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/*.csv')
for file in silvio_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))#st deviation
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    times[unique_hour] = (week, day, hour, var) # the indices of this tuple are used for plotting in the loop below.
    #print(unique_hour)
unique_hours = list(range(min(times), max(times)))
for unique_hour in unique_hours:
    if unique_hour not in times:
        week = unique_hour // (7*24)
        day  = unique_hour // 24 - week * 7
        hour = unique_hour - (week * 7 + day) * 24
        times[unique_hour] = (week, day, hour, np.NaN)
silvio_times=times
tsilvio_times=silvio_times


rey_times
silvio_times[hour][3]
silvio_times[3]
[]

len(silvio_times)
len(s_var)
s_var=[]
for hour in silvio_times:
    s_var.append(silvio_times[hour][3])
    
#Silvio's varianced discretized, then low pass filter applied below as lpf_var
import glob
import pandas as pd
dvariance=[]
for file in silvio_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))#std deviation
    if var<.003:
        var=0
        sleep_var.append(var)
    elif var>=.003:
        var=1
        sleep_var.append(var)
    dvariance.append(var)
s_dvariance=dvariance#**MAKE COPY

lpf_var=s_dvariance#**FROM COPY
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
s_lpf_var=lpf_var         

#Rey's time and variance
times = {}
rey_list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/o6bokidk/accelerometer/*.csv')
for file in rey_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))#std deviation
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    times[unique_hour] = (week, day, hour, var) # the indices of this tuple are used for plotting in the loop below.
    #print(unique_hour)
unique_hours = list(range(min(times), max(times)))
for unique_hour in unique_hours:
    if unique_hour not in times:
        week = unique_hour // (7*24)
        day  = unique_hour // 24 - week * 7
        hour = unique_hour - (week * 7 + day) * 24
        times[unique_hour] = (week, day, hour, np.NaN)
rey_times=times

#Rey's varianced discretized, then low pass filter applied below as lpf_var
dvariance=[]
for file in rey_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))
    if var<.15:
        var=0
    elif var>=.15:
        var=1
    dvariance.append(var)
r_dvariance=dvariance#**MAKE COPY

lpf_var=r_dvariance#**FROM COPY
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
r_lpf_var=lpf_var        

#Patrick's time and variance
times = {}
pat_list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/b6v2i419/accelerometer/*.csv')
for file in pat_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))#st deviation
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    times[unique_hour] = (week, day, hour, var) # the indices of this tuple are used for plotting in the loop below.
    #print(unique_hour)
unique_hours = list(range(min(times), max(times)))
for unique_hour in unique_hours:
    if unique_hour not in times:
        week = unique_hour // (7*24)
        day  = unique_hour // 24 - week * 7
        hour = unique_hour - (week * 7 + day) * 24
        times[unique_hour] = (week, day, hour, np.NaN)
pat_times=times
tpat_times=pat_times
rey_times

#Patrick's varianced discretized, then low pass filter applied below as lpf_var
dvariance=[]
for file in rey_list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    var=np.sqrt(sum(df.var(axis=0)))
    if var<.003:
        var=0
    elif var>=.003:
        var=1
    dvariance.append(var)
p_dvariance=dvariance#**MAKE COPY

lpf_var=p_dvariance#**FROM COPY
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
p_lpf_var=lpf_var        

#HEAT MAP********************************************************
def polygon(unique_hour, given_week, r, g, b, rb, gb, bb):
    week = unique_hour // (7*24)
    day  = unique_hour // 24 - week * 7
    hour = unique_hour - (week * 7 + day) * 24
    if week == given_week:
                    ax.add_patch(
                    patches.Rectangle((hour,day), # (x,y)
                    1,                 # width
                    1,                 # height
                    edgecolor = rgb(rb, gb, bb),
                    facecolor=rgb(r, g, b)
                    )
                )
    
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
#given_week=24 #yellow and blue borders, indicating my missing data on week 24?
silvio_times

def plot_week(given_week):
    given_week=27
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for key in all_keys:
        if key in rey_times:
            r = int(rey_times[key][3] > 5)
            rb = 1
        else:#border color
            r = 1
            rb = 0
        if key in pat_times:
            g = int(pat_times[key][3] > 5)
            gb = 1
        else:
            g = 1
            gb = 0
        if key in silvio_times:
            b = int(silvio_times[key][3] > 0.3)
            bb = 1
        else:
            b = 1
            bb = 0
        week = unique_hour // (7*24)
        day  = unique_hour // 24 - week * 7
        hour = unique_hour - (week * 7 + day) * 24
        if week == given_week:
            ax.add_patch(
                patches.Rectangle((hour,day), # (x,y)
                    1,                 # width
                    1,                 # height
                    edgecolor = rgb(rb, gb, bb),
                    facecolor=rgb(r, g, b)
                )
            )
        polygon(key, given_week, r, g, b, rb, gb, bb)
    plt.xlim(0,24)
    plt.ylim(0,7)
    plt.savefig("Heat Map Week 27.pdf")
    
        #plt.savefig("Heat Map, Repeated Data.pdf")
        
polygon(key, given_week, .5,.5,.5,.5,.5,.5)
for given_week in range(24,27):
    print(given_week)
    plot_week(given_week)
    
plot_week(24)
min(pat_times)
min(silvio_times)
pat_times.values()

#Individual heat map
def plot_heatmap(week):
    week=27
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for unique_hour in times:
        hour_data = times[unique_hour]
        if hour_data[0]==week: #
            color = min(hour_data[3], 1) # this ensures my variance is between 0 and 1.
            ax.add_patch(
                patches.Rectangle(
                    (hour_data[2], hour_data[1]), # (x,y)
                    1,                 # width
                    1,                 # height
                    edgecolor = "none",
                    facecolor=rgb(color, color, color)
                )
            )
    plt.xlim(0,24)
    plt.ylim(0,7)
    fig.savefig("C:/Users/Silvio/Documents/Python" + str(week) + ".pdf", bbox_inches='tight')
    plt.savefig("Rey Week 28.pdf")

unique_weeks = set([times[time][0] for time in times])
for week in unique_weeks:
    print(week)
    plot_heatmap(week)
    #if its na, then add border

#low pass filter plots
length = list(range(0,len(s_lpf_var)))#
plt.plot(length,s_lpf_var,"ko",linewidth=2,markersize=1);
plt.title('Variance with Low Pass Filter',fontsize=15)
plt.xlabel('Time (Hours) Since Day 1',fontsize=12)
plt.ylabel('Discretized Variance',fontsize=12)
plt.xticks(length[::10],silvio_t[::10])
plt.savefig("Variance Low Pass Silvio.pdf")

list(pat_times.keys())[0]
#Want to coordinate the times for all values into same start time
#while the first key, which indicate the hours, for Silvio and Pat is greater than 
#Rey's , who has the latest start time, remove the first key
#must create a list from dictionary bc dictionaries have no order 
#PROBLEM: Doesn't remove NA's! because doesn't detect them in 
from collections import deque

ptimes_array=np.array(pat_times.keys())
p_var=[pat_times[key][3] for key in pat_times]

temp=[]
dictlist=[]
for key, value in dict.iteritems():
    silvio_times = [key,value]
    dictlist.append(silvio_times)

pat_times    = {time: pat_times[time]    for time in pat_times    if time >= min(rey_times)}
silvio_times = {time: silvio_times[time] for time in silvio_times if time >= min(rey_times)}

while list(pat_times.keys())[0] and list(silvio_times.keys())[0] < list(rey_times.keys())[0]:
    pat_times.pop(list(pat_times.keys())[0],None)
    silvio_times.pop(list(silvio_times.keys())[0],None)
    for hour in silvio_times:
        if silvio_times[hour][3] is np.NaN:
            silvio_times.pop(hour)
    for hour in pat_times:
        if pat_times[hour][3] is np.NaN:
            pat_times.pop(hour)



l=deque([1,2,3,4])
l.popleft()

min(silvio_times)

while l[2]<10:
    




p=deque(list(pat_times.keys()))
p.poplef

silvio_times.pop(4179)   
tsilvio_times.pop(4192)
tsilvio_times
tpat_times
pat_times
silvio_times
rey_times
silvio_times[4192][3] is np.NaN

#RGB for heatmap
def rgb(r, g, b):
    hex_string, output = "0123456789abcdef", "#"
    for pigment in (r, g, b):
        hex_val = min(int(pigment*256), 255)
        output = output + hex_string[hex_val//16] + hex_string[hex_val%16]
    return output

### Here is a plotting example, where a 10x10 grid is filled in with entirely random colors.###
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
for i in range(10):
    for j in range(10):
        ax.add_patch(
            patches.Rectangle(
                (i,j), # (x,y)
                1,     # width
                1,     # height
                edgecolor = "none",
                facecolor=rgb(random.random(), random.random(), random.random())
            )
        )
    
plt.xlim(0,10)
plt.ylim(0,10)
fig.savefig('Quilt Heat Map', bbox_inches='tight')

24*7
### Here is a plotting example with hypothetical data for Rey, Danielle, and Silvio.###
n = 168 # total number of hours of data available
rey_data      = [int(random.random()>0.5) for i in range(n)]
danielle_data = [int(random.random()>0.5) for i in range(n)]
silvio_data   = [int(random.random()>0.5) for i in range(n)]

hour = [i%24 for i in range(n)]#rows
day = [i//24 for i in range(n)]#columns

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
for i in range(n):
    ax.add_patch(
        patches.Rectangle(
            (hour[i],day[i]), # (x,y)
            1,                 # width
            1,                 # height
            edgecolor = "none",
            facecolor=rgb(rey_data[i], danielle_data[i], silvio_data[i])
        )
    )
        
5/8
pat
plt.xlim(0,24)
plt.ylim(0,max(day)+1)
fig.savefig('Data Example Patrick', bbox_inches='tight')

#REPEATED DATA HEAT MAP
#somehow need to make this lpf_var data iterate
n = 168 # total number of hours of data available
#these are 3 data sets with just the last 5 values different because I don't have
#danielle's and rey's data, so I just duplicated it
#for i in all_keys:


hour = [i%24 for i in range(n)]#rows
day = [i//24 for i in range(n)]#columns

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
for i in range(n):
    ax.add_patch(
        patches.Rectangle((hour[i],day[i]), # (x,y)
            1,                 # width
            1,                 # height
            edgecolor = "none",
            facecolor=rgb(danielle_data[i], silvio_data[i], rey_data[i])
        )
    )
     
plt.xlim(0,24)
plt.ylim(0,max(day)+1)
plt.title('Activity Levels: Variance of Phone Accelerometer',fontsize=14)
plt.xlabel('Time (Hours)',fontsize=12)
plt.ylabel('Days of the Week',fontsize=12)
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24])
plt.yticks(['Sun','Mon','Tue','Wed','Thu','Fri','Sat'])
plt.show()
plt.savefig("Heat Map, Repeated Data.pdf")
#plt.ylabel('Discretized Variance',fontsize=12)



plt.yticks([1,2,3,4,5,6])
clabels=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
ax.set_xticklabels(rlabels, minor=False)
ax.set_yticklabels(clabels, minor=False)
#silvio_data=silvio_data+[0,0,0,0,0]

fig.savefig('Data Example Patrick', bbox_inches='tight')

##HEATMAP 2

      
#goes through missing hours and adds the consecutive integers
#Issue with this is that it loops through each non-consecutive number first
#but only fills in the first value in a range of missing values. Then the loop stops
#once it reaches end. In order to fill all values, I have to manually run the for loop
#many times.
timelist=list(times)
for hour in range(len(timelist)):
    if timelist[hour]==timelist[-1]:#if last hour, just pass
        print("A")
    elif timelist[hour+1]!=timelist[hour]+1:#if the next number is not consecutive, add this
        timelist.append(timelist[hour]+1)#number to the list
    timelist=sorted(timelist,key=int)


#This while loop infinitely adds values because it doesn't know to stop at the last value,
#but if I put break in the first if statement, it doesn't fill in all values
timelist=list(times)
while timelist[hour+1]!=timelist[hour]+1:
    if  timelist[hour]!=timelist[-1]:
        pass
        #repeat and loop if this is true until no more numbers to fill in
    for hour in range(len(timelist)):
        timelist.append(timelist[hour]+1)
        timelist=sorted(timelist,key=int)

del timelist[-1]#need to run this after while loop to 

     
timelist=sorted(timelist,key=int)        
templist = [25, 50, 100, 150, 200, 250, 300, 33]
templist=sorted(templist, key=int) 

#if the hour is already in times, then skip it
#if the hour is not in times, then add it, and add the null values into tuples
for i in timelist:#iterate timelist
    if i in times:
        pass
    else:
        #times[i]=()
        date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        week = date.isocalendar()[1]
        day = date.weekday()
        hour = date.hour
        unique_hour = (week * 7 + day) * 24 + hour
        times[i]=(week,day,hour,np.NaN)
        times[unique_hour] = (week, day, hour, np.NaN)
        

#add missing values to dictionary, times[4372]=(week,day,hour,null)
#4380-4179; 201 hours
#201/24; about 8 days

def plot_heatmap(week):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for unique_hour in times:
        hour_data = times[unique_hour]
        if hour_data[0]==week: #
            color = min(hour_data[3], 1) # this ensures my variance is between 0 and 1.
            ax.add_patch(
                patches.Rectangle(
                    (hour_data[2], hour_data[1]), # (x,y)
                    1,                 # width
                    1,                 # height
                    edgecolor = "none",
                    facecolor=rgb(color, color, color)
                )
            )
    plt.xlim(0,24)
    plt.ylim(0,7)
    fig.savefig("C:/Users/Patrick/Desktop/data_" + str(week) + ".pdf", bbox_inches='tight')

#save plots
unique_weeks = set([times[time][0] for time in times])
for week in unique_weeks:
    print(week)
    plot_heatmap(week)











