# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:01:58 2017

@author: Silvio
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:55:34 2017

@author: Silvio
"""
############START HERE#######################
#Sleep Time from survey
import re
import numpy as np
import pandas as pd
import glob
import re
import datetime as dt
import dateutil.parser as dparser

##Dictionary of Tuples for surveys
import datetime
columns=['question id','question type','question text','question answer options','Sleep Times']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-21 15_43_46.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
sleep=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
print(sleep)
silvio_list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/*.csv')
survey_times={}
type(sleep)
for file in silvio_list_of_files:#loop through to add sleep times of each day to Sleep Times data frame
    columns=['question id','question type','question text','question answer options','Sleep Times']#make sure these column names match the previously defined names!
    survey=pd.read_csv(file,header=0,sep=',',names=columns)
    survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
    store=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
    sleep = sleep.append(store, ignore_index=True)
sleep=sleep.drop(sleep.index[[0,1]])#removing the repeated file that was read in the loop#number of files
sleep.index=sleep.index-1
sleep= sleep[pd.notnull(sleep['Sleep Times'])]#removes NaN's

sleep=sleep['Sleep Times'].tolist()#converts dic to list
#date_str=miltime('on Jun 03, 02010 at 10:22PM')#can put this into miltime function, with further
#modifications
mtime=[]
def miltime(date_str):
    date_str
    date=dparser.parse(date_str)
    # 2010-06-03 22:22:00
    date=(date.strftime('%H:%M'))
    print(date)
    mtime.append(date)
    
    #to military time, but won't work without manually taking out strings
mtime=[]#military time
for i in range(len(sleep)):
#    print(sleep[i])
    miltime(sleep[i])
#==============================================================================
# FUNCTION
#==============================================================================
dec_time=[]
def time_string_to_decimals(time_string):
    """Converts the time to an integer of hours and minutes as decimals """
    fields = time_string.split(":")
    hours = fields[0] if len(fields) > 0 else 0.0
    minutes = fields[1] if len(fields) > 1 else 0.0
    seconds = fields[2] if len(fields) > 2 else 0.0
    final= float(hours) + (float(minutes) / 60.0) + (float(seconds) / pow(60.0, 2))
    dec_time.append(final)
time_string_to_decimals("1:12")

#WIll convert time to decimals for the data frame, but need to convert to military time first
dec_time=[]
for time in range(len(mtime)):
    time_string_to_decimals(mtime[time])

#==============================================================================
#made copies below to run code 
copy_silvio_files_survey=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning Copies/*.csv')
unique_hour_survey=[]
for h in range(len(mtime)):
    if h%2==0:#if even, or hour to sleep
#        print(mtime[h])#prints all times went to sleep
#        print(file)
        if dec_time[h]<12:#if went to sleep past midnight
            date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",copy_silvio_files_survey[h]).group(1))#***make sure testing correct file
            sep=" "
            date_string=date_string.split(sep,1)[0]#get only date from file, without time
            date=datetime.datetime.strptime(date_string+" " +mtime[h], "%Y-%m-%d %H:%M")
            week = date.isocalendar()[1]
            day = date.weekday()
            hour = date.hour
            unique_hour = (week * 7 + day) * 24 + hour
            unique_hour_survey.append(unique_hour)
        else:#if before midnight, change to day before
            #hour=0 (1 am first sleep time) -->test
            date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",copy_silvio_files_survey[h]).group(1))
            sep=" "
            date_string=date_string.split(sep,1)[0]
            ##ISSUE
            date=datetime.datetime.strptime(date_string+" " +mtime[h], "%Y-%m-%d %H:%M")
            #FUNCTION ROUNDS DOWN TO HOUR, DISREGARDING MINUTES
            yesterday=date+datetime.timedelta(days=-1)#changes to day of yesterday
            week = yesterday.isocalendar()[1]
            day = yesterday.weekday()
            hour = yesterday.hour
            unique_hour = (week * 7 + day) * 24 + hour
            unique_hour_survey.append(unique_hour)
    if h%2!=0:
        date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",copy_silvio_files_survey[h]).group(1))#***make sure testing correct file
        sep=" "
        date_string=date_string.split(sep,1)[0]#get only date from file, without time
        date=datetime.datetime.strptime(date_string+" " +mtime[h], "%Y-%m-%d %H:%M")
        week = date.isocalendar()[1]
        day = date.weekday()
        hour = date.hour
        unique_hour = (week * 7 + day) * 24 + hour
        unique_hour_survey.append(unique_hour)
     

#==============================================================================
#     
#==============================================================================
#creating dictionary for survey sleep times
survey_times={}
for file in silvio_list_of_files:   
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    #what does this do
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    survey_times[unique_hour] = (week, day, hour, 1)#must change day and week to day before
#code below adds rest of hours and puts nan for those in between
unique_hours = list(range(min(survey_times), max(survey_times)))
for unique_hour in unique_hours:
    if unique_hour not in survey_times:
        week = unique_hour // (7*24)
        day  = unique_hour // 24 - week * 7
        hour = unique_hour - (week * 7 + day) * 24
        survey_times[unique_hour] = (week, day, hour, 1)

#Create for loop where skip through even numbers, if even then find range from that i to next i
#and append to new list
unique_survey_new=[]#makes multiples lists of ranges of sleep times
for hour in range(len(unique_hour_survey)):
    if hour %2==0:
        unique_survey_new.append(list(range(unique_hour_survey[hour],unique_hour_survey[hour+1]+1)))
    #if range is 0 (no sleep), then output values in a list for those (NaNs)

#puts all in one list
unique_survey_new = [item for sublist in unique_survey_new for item in sublist]
#unique_survey_new.remove(4440)#removing hour when no sleep

for i in survey_times.keys():
    if i in unique_survey_new:
        survey_times[i]=(survey_times[i][0],survey_times[i][1],survey_times[i][2],0)

#==============================================================================
#     FIN________________________
#==============================================================================

columns=['question id','question type','question text','question answer options','Sleep Times']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-21 15_43_46.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
#**wanted to define this data frame before the loop in order to append to this data frame,
#could also learn to append to an empty data frame!
sleep=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])

list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/*.csv')
c=0
for file in list_of_files:#loop through to add sleep times of each day to Sleep Times data frame
    columns=['question id','question type','question text','question answer options','Sleep Times']#make sure these column names match the previously defined names!
    survey=pd.read_csv(file,header=0,sep=',',names=columns)
    survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
    store=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
    c+=1#count number of files
    sleep = sleep.append(store, ignore_index=True)
   # sleep['Sleep Times'] = sleep['Sleep Times'].map(lambda x: x.rstrip('AaMm'))
sleep=sleep.drop(sleep.index[[0,1]])#removing the repeated file that was read in the loop
c#number of files
sleep.index=sleep.index-1
print(sleep)

x="8:00 am".toupper()
x=x.split ("A")[0]

#==============================================================================
# ##################################################
#==============================================================================
columns=['question id','question type','question text','question answer options','Sleep Times']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-21 15_43_46.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
#**wanted to define this data frame before the loop in order to append to this data frame,
#could also learn to append to an empty data frame!
sleep=survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
wake=survey.drop(survey.index[[0,1,3,4,5,6,7,8,9,10,11]])
type(sleep)
#TASK : 1- could create a data frame with second column as wake times
# or : 2- could create a list of tuples

###1:
sLength=len(sleep['Sleep Times'])
sleep['Wake Up Times'] = pd.Series(wake, index=sleep.index)
sleep

list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/*.csv')
c=0
for file in list_of_files:#loop through to add sleep times of each day to Sleep Times data frame
    columns=['question id','question type','question text','question answer options','Sleep Times']#make sure these column names match the previously defined names!
    survey=pd.read_csv(file,header=0,sep=',',names=columns)
    survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
    sleep=survey.drop(survey.index[[0,2,3,4,5,6,7,8,9,10,11]])
    wake=survey.drop(survey.index[[0,1,3,4,5,6,7,8,9,10,11]])
#    sLength=len(sleep['Sleep Times'])
#    sleep['Wake Up Times'] = pd.Series(wake, index=sleep.index)
#    store=sleep
    sleep=np.array(list([sleep]+[wake]))
    c+=1#count number of files
    sleep = sleep.append(store, ignore_index=True)
sleep=sleep.drop(sleep.index[[0,1]])#removing the repeated file that was read in the loop
S_All_Sleep=np.array(list(zip(*[SHour]+[SWent_sleep]+[SUp])))

c#number of files
sleep.index=sleep.index-1
print(sleep)


#==============================================================================
# 
#==============================================================================

for file in silvio_list_of_files:
#st deviation
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    times[unique_hour] = (week, day, hour, var)

#get which hour from zero to 24 and whether asleep (indicator)
#dictionary of tuples:unique hour as keys, hour in day, indicator variable
#plots: sleep over calendar time
#heat map for correlation between acc, fitbit, survey
#correlation plot
#statistical summary (lm,)
#unique_hour   week  day   hour value
#prepopulate values to 1 if its in range of hour then change to 0 (sleep)
#"a".toupper()
#"A"

tuple(list(sleep['Sleep Times']))

subset = sleep[['Sleep Times']]
tuples = [tuple(x) for x in subset.values]

20000/12
#5 , 10 min intervals
#
#SLeep time from phone accelerometer variance
Rtimes = list(rey_times.keys())
RTime_of_sleep=[]
for i in Rtimes:
    if rey_times[i][3]<.15:
        RTime_of_sleep.append(i)
        
Ptimes = list(pat_times.keys())
PTime_of_sleep=[]
for i in Ptimes:
    if pat_times[i][3]<.15:
        PTime_of_sleep.append(i)

Stimes = list(silvio_times.keys())
STime_of_sleep=[]
for i in Stimes:
    if silvio_times[i][3]<.003:
        STime_of_sleep.append(i)
        
max(silvio_times)
SWent_sleep=[]
SUp=[]
SHour=[]
for v in range(len(STime_of_sleep)):
    if STime_of_sleep[v] == STime_of_sleep[0]:
        if STime_of_sleep[v]==STime_of_sleep[v+1]-1:
            print("Went to sleep at " + str(silvio_times[(STime_of_sleep[v])][2]))
            SWent_sleep.append(silvio_times[(STime_of_sleep[v])][2])
            SHour.append(STime_of_sleep[v])
    elif STime_of_sleep[v] == STime_of_sleep[-1]:
        if STime_of_sleep[v] == STime_of_sleep[v-1]+1:
           print("Woke up at " + str(silvio_times[(STime_of_sleep[v])][2]))
           SUp.append(silvio_times[(STime_of_sleep[v])][2])
            
    elif STime_of_sleep[v-1] != STime_of_sleep[v]-1 and STime_of_sleep[v+1] == STime_of_sleep[v]+1:
        print("Went to sleep at " + str(silvio_times[(STime_of_sleep[v])][2]))
        SWent_sleep.append(silvio_times[(STime_of_sleep[v])][2])
        SHour.append(STime_of_sleep[v])
        
    elif STime_of_sleep[v-1] == STime_of_sleep[v]-1 and STime_of_sleep[v+1] != STime_of_sleep[v]+1:
        print("Woke up at " + str(silvio_times[(STime_of_sleep[v])][2]))
        SUp.append(silvio_times[(STime_of_sleep[v])][2])
S_All_Sleep=np.array(list(zip(*[SHour]+[SWent_sleep]+[SUp])))
X=[]
Woke=[]
Sleep=[]
for i in range(len(S_All_Sleep)):
    Sleep.append(S_All_Sleep[i][1])
    Woke.append(S_All_Sleep[i][2])
    X.append(S_All_Sleep[i][0])
plt.plot(X,Woke, "bo")
plt.plot(X,Sleep,  "bo")
for (i,j) in zip(Sleep,Woke):
    plt.plot((i,j),color = 'g')

Sleep_Sum=[]
for i in range(len(Woke)):
    Sleep_Sum.append(Woke[i]-Sleep[i])

########
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

frame = pd.DataFrame({'a' : ['the cat is blue', 'the sky is green', 'the dog is black']})
frame['b'] = frame.a.str.contains("dog") | frame.a.str.contains("cat") | frame.a.str.contains("fish")

sleep['Sleep Times'].str.contains('sleep')



sleep[39]
random=[1,2,3,4,5]
for i in range(len(random)):
    print(random[i])

