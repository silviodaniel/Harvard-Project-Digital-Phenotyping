# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:55:34 2017

@author: Silvio
"""

#Next task: trying to extract survey data on sleep and store into data frame for all days
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
