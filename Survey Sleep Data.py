# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:55:34 2017

@author: Silvio
"""

#Next task: trying to extract survey data on sleep and store into data frame for all days
import pandas as pd
columns=['question id','question type','question text','question answer options','answer']
survey=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/survey_answers/Morning/2017-06-21 15_43_46.csv',header=0,sep=',',names=columns)
survey.drop(survey.columns[[0,1,2,3]],axis=1,inplace=True)
#ans=sleep['answer'].values
#answers=[ans[1], ans[2]]#will create a list, but how do we want to store them?
type(survey)
survey.drop(survey.index[[0,3,4,5,6,7,8,9,10,11]])
sleep=survey
sleep
ans

columns=['Questions','Answers']
df_ = pd.DataFrame(columns=columns)
df=pd.DataFrame(sleep,columns=columns)
pd.DataFrame.add()