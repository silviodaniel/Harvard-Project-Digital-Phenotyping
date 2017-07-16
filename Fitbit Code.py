# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:37:56 2017

@author: Silvio
"""
import re
import pandas as pd
import glob
import re
import datetime
import datetime as dt
import dateutil.parser as dparser
import numpy as np
##Dictionary of Tuples for Fitbit
columns=['Sleep','Awake']#make sure these column names match the previously defined names!
silvio_fit=pd.read_csv('C:/Users/Silvio/Documents/Python/Fitbit/Silvio/06-21-2017.csv',header=0,sep=',',names=columns)
silvio_list_files=glob.glob('C:/Users/Silvio/Documents/Python/Fitbit/Silvio/*.csv')
silvio_fitbit={}
for file in silvio_list_files: 
    columns=['Sleep','Awake']#make sure these column names match the previously defined names!
    fitdata=pd.read_csv(file,header=0,sep=',',names=columns)
    silvio_fit=silvio_fit.append(fitdata, ignore_index=True)
    #dictionary code below
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%m-%d-%Y")
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    silvio_fitbit[unique_hour] = (week,day,hour,1)

silvio_fit=silvio_fit.drop(silvio_fit.index[[0,0]])#removing the repeated file that was read in the loop#number of files
print(silvio_fit)

#need to mark the day went to sleep and not remove bc need to loop through that file later        
silvio_fit.loc[9,'Sleep']="12 am"
silvio_fit.loc[9,'Awake']="12 am"
silvio_fit_sleep=silvio_fit['Sleep'].tolist()#converts dic to list
silvio_fit_wake=silvio_fit['Awake'].tolist()

silvio_fit_comb=[]#combine the two lists
for hour in range(len(silvio_fit_wake)):
    silvio_fit_comb.append(silvio_fit_sleep[hour])
    silvio_fit_comb.append(silvio_fit_wake[hour])
#replacing nan's,marking them as 1am . later, will change those back to NaN, will put day as NaN
for hour in range(len(silvio_fit_comb)):
    if silvio_fit_comb[hour] is np.nan:
        silvio_fit_comb[hour]="1 am"
    if silvio_fit_comb[hour] is np.nan:
        silvio_fit_comb[hour]="1 am"

#military time conversion
mtime=[]
def miltime(date_str):
    date_str
    date=dparser.parse(date_str)
    # 2010-06-03 22:22:00
    date=(date.strftime('%H:%M'))
    print(date)
    mtime.append(date)
    
mtime=[]#military time
for i in range(len(silvio_fit_comb)):
#    print(silvio_fit_comb[i])
    miltime(silvio_fit_comb[i])

#Time as decimals
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

copy_silvio_files_fit=glob.glob('C:/Users/Silvio/Documents/Python/Fitbit/Silvio Copies/*.csv')
unique_hour_fit=[]
for h in range(len(mtime)):
    if h%2==0:#if even, or hour to sleep
#        print(mtime[h])#prints all times went to sleep
#        print(file)
        if dec_time[h]<12:#if went to sleep past midnight
            date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",copy_silvio_files_fit[h]).group(1))#***make sure testing correct file
            sep=" "
            date_string=date_string.split(sep,1)[0]#get only date from file, without time
            date=datetime.datetime.strptime(date_string+" " +mtime[h], "%m-%d-%Y %H:%M")
            week = date.isocalendar()[1]
            day = date.weekday()
            hour = date.hour
            unique_hour = (week * 7 + day) * 24 + hour
            unique_hour_fit.append(unique_hour)
        else:#if before midnight, change to day before
            #hour=0 (1 am first sleep time) -->test
            date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",copy_silvio_files_fit[h]).group(1))
            sep=" "
            date_string=date_string.split(sep,1)[0]
            ##ISSUE
            date=datetime.datetime.strptime(date_string+" " +mtime[h], "%m-%d-%Y %H:%M")
            #FUNCTION ROUNDS DOWN TO HOUR, DISREGARDING MINUTES
            yesterday=date+datetime.timedelta(days=-1)#changes to day of yesterday
            week = yesterday.isocalendar()[1]
            day = yesterday.weekday()
            hour = yesterday.hour
            unique_hour = (week * 7 + day) * 24 + hour
            unique_hour_fit.append(unique_hour)
    if h%2!=0:
        date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",copy_silvio_files_fit[h]).group(1))#***make sure testing correct file
        sep=" "
        date_string=date_string.split(sep,1)[0]#get only date from file, without time
        date=datetime.datetime.strptime(date_string+" " +mtime[h], "%m-%d-%Y %H:%M")
        week = date.isocalendar()[1]
        day = date.weekday()
        hour = date.hour
        unique_hour = (week * 7 + day) * 24 + hour
        unique_hour_fit.append(unique_hour)


#4440 remove, 4705,4729 keep as NaN
#should output 4703 if h=38
#should output 4249 if h=0; 
#==============================================================================
#     
#==============================================================================
#creating dictionary for survey sleep times
import re
import numpy as np
fit_times={}
silvio_list_of_fits=glob.glob('C:/Users/Silvio/Documents/Python/Fitbit/Silvio/*.csv')
for file in silvio_list_of_fits:   
    date_string = re.sub("_",":",re.match(r"^.*\\(.*)\.csv.*$",file).group(1))
    date = datetime.datetime.strptime(date_string, "%m-%d-%Y")
    #what does this do
    week = date.isocalendar()[1]
    day = date.weekday()
    hour = date.hour
    unique_hour = (week * 7 + day) * 24 + hour
    fit_times[unique_hour] = (week, day, hour, 1)#must change day and week to day before
#code below adds rest of hours and puts nan for those in between
unique_hours = list(range(min(fit_times), max(fit_times)))
for unique_hour in unique_hours:
    if unique_hour not in fit_times:
        week = unique_hour // (7*24)
        day  = unique_hour // 24 - week * 7
        hour = unique_hour - (week * 7 + day) * 24
        fit_times[unique_hour] = (week, day, hour, 1)

#Create for loop where skip through even numbers, if even then find range from that i to next i
#and append to new list
unique_fit_new=[]#makes multiples lists of ranges of sleep times
for hour in range(len(unique_hour_fit)):
    if hour %2==0:
        unique_fit_new.append(list(range(unique_hour_fit[hour],unique_hour_fit[hour+1]+1)))
    #if range is 0 (no sleep), then output values in a list for those (NaNs)
    #if 

#puts all in one list
unique_fit_new = [item for sublist in unique_fit_new for item in sublist]
#unique_survey_new.index(4440)
unique_fit_new.remove(4440)#removing hour when no sleep

for i in fit_times.keys():
    if i in unique_fit_new:
        fit_times[i]=(fit_times[i][0],fit_times[i][1],fit_times[i][2],0)
    if i == 4705 or i==4729:
        fit_times[i]=(fit_times[i][0],fit_times[i][1],fit_times[i][2],np.NaN)

hour=4704
while hour<4752:
    fit_times[hour]=(fit_times[hour][0],fit_times[hour][1],fit_times[hour][2],np.NaN)
    hour+=1
    
    survey_times#4703-4710, 4681-4688
i=4846
fit_times.keys()
        






