# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:55:34 2017

@author: Silvio
"""

#Sleep Time from survey
import pandas as pd
import glob
columns=['question id','question type','question text','question answer options','Sleep Times']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-21 15_43_46.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
#**wanted to define this data frame before the loop in order to append to this data frame,
#could also learn to append to an empty data frame!
sleep=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
sleep
list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/*.csv')
c=0
for file in list_of_files:#loop through to add sleep times of each day to Sleep Times data frame
    columns=['question id','question type','question text','question answer options','Sleep Times']#make sure these column names match the previously defined names!
    survey=pd.read_csv(file,header=0,sep=',',names=columns)
    survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
    store=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
    sleep = sleep.append(store, ignore_index=True)
    c+=1#count number of files
sleep=sleep.drop(sleep.index[[0,1]])#removing the repeated file that was read in the loop
c#number of files
sleep.index=sleep.index-1
print(sleep)

20000/12
#5 , 10 min intervals
#
#SLeep time from phone accelerometer variance
import numpy as np
x=np.array(Time_of_sleep)
x.where(0)

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
        
        ###
c=dvariance
c=variance
def mod(a,b):
    return a%b    
t=[3]
for i in t:
    if len(t)<len(c):
        t.append(mod(i+1,24))
    else:
        exit

#Time of sleep for original data
Time_of_sleep=[]
for i in c:
    if i<.003:
        Time_of_sleep.append(t[c.index(i)])

#Time of sleep for binary data 
dvariance
sleeptime=[i for i, x in enumerate(dvariance) if x==0]
Time_of_sleep=[]
for pos in sleeptime:
    print(t[pos])
    Time_of_sleep.append(t[pos])
    
dvariance[128]
t[sleeptime.index(5)]
#for loop for all these values, get values from dvariance and append to new list

testlist=[1, 2, 3, 5, 3, 1, 2, 1, 6]
[i for i,x in enumerate(testlist) if x == 1]
[0, 5, 7]

t[dvariance.index(1)]


dvariance[3]
dvariance.index(3)
#6-11, 5-10, 5-9,4-9,7-11,6-11
# More cosmetic. Gives us "went to sleep at_" and "woke up at_"
g=[]
Time_of_sleep[-1]
#why does it run the position zero multiple times? because there may be multiple values 
#that equal the time at zero
Time_of_sleep.index(Time_of_sleep[7])
Time_of_sleep.index(6)
len(Time_of_sleep)
Time_of_sleep[5-1]==Time_of_sleep[5]-1
Time_of_sleep[5+1] != Time_of_sleep[5]+1
str(Time_of_sleep[5])
#never runs B either


for index, s in enumerate(Time_of_sleep):
    print index,s
##
for v in range(len(Time_of_sleep)):
    if Time_of_sleep[v] == Time_of_sleep[0]:#at first point, if next value is consecutive..
        if Time_of_sleep[v]==pos=0
        if Time_of_sleep[v]==Time_of_sleep[v+1]-1:
            print("Went to sleep at " + str(Time_of_sleep[v]))#sleep!
            print("A")
    elif Time_of_sleep[v] == Time_of_sleep[-1]:
        if Time_of_sleep[v] == Time_of_sleep[-1]+1:
           print("Woke up at " + str(Time_of_sleep[v]))
           print("B")        
    elif Time_of_sleep[v-1] != Time_of_sleep[v]-1 and Time_of_sleep[v+1] == Time_of_sleep[v]+1:
        print("Went to sleep at " + str(Time_of_sleep[v]))
        print("C")
    elif Time_of_sleep[v-1] ==Time_of_sleep[v]-1 and Time_of_sleep[v+1] != Time_of_sleep[v]+1:
        print("Woke up at " + str(Time_of_sleep[v]))
        print("D")

for index, s in enumerate(Time_of_sleep):
    print index,s

#NOTES
#integrate over time, define a rule and discretize the data
#
x=(range(0,10))
#x[::3]x``


#1 plt.polygon, sheet 24x7, get polygon function, search heatplot function,
#use rgb values tp specify colors 
#2 interval for activity and inactivity for time and 0 and 1s , Rey
#3 low pass filter: don't use a for loop, use for loop that deems each point for lowpassfilter
#hi and low,, take estimates of previous step
#specify width and sum if sum is 2 or greater then 
#in for loop, width =2 , if sum 2 or greater, then 1, 

#show discretized graph when explaining consecutive hours
#how to do low pass
#############################
#NOTES FROM GROUPS
#regular expressions : RStudio
#in R, %>% from dplyer (Andrea)

#Next task: trying to extract survey data on sleep and store into data frame for all days
#1- import 1 file and get the data frame
#2 create loop and import all files and add the times to the data frame
import pandas as pd
columns=['question id','question type','question text','question answer options','answer']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-21 15_43_46.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
sleep=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
sleep
#sleep = sleep.append(sleep, ignore_index=True)
#sleep

columns=['question id','question type','question text','question answer options','answer']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-22 13_39_29.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
store=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
sleep = sleep.append(store, ignore_index=True)
sleep


    
columns=['Questions','Answers']
df_ = pd.DataFrame(columns=columns)
df=pd.DataFrame(sleep,columns=columns)
#pd.DataFrame.add(DataFrame,axis=1,'hi')


survey.loc[-1]=[1]
survey.index=survey.index+1
survey
survey=survey.sort()
type(survey)

list=['abc','123','bcd']
list.sort()






