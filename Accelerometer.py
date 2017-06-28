# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:25:09 2017

@author: Silvio
"""

#Reduce size of data
#abs value of extreme values 
#take 3 variances of 3 dimensions, add; sum of squares of them, mean,
#make function that takes a whole file and reduces by hour
#Giulina Fortweiler

#cross correlation of sleep estimates

#files: os.file
#np.std; np.mean ; np.sum by hour
os.getcwd()
import pandas as pd
columns=['time stamp','UTC time','accuracy','x','y','z']
df=pd.read_csv('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/2017-06-18 03_00_00.csv',header=0,sep=',',names=columns)
x=df['x'].values
y=df['y'].values
z=df['z'].values
df.head()
df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
sx=sum(x**2)
sy=sum(y**2)
sz=sum(z**2)
sz
sx+sz+sy
#sum of squares is 4164.729344982421

mean=(np.mean(x)+np.mean(y)+np.mean(z))/3
#mean is -0.32741857769006366
np.mean(df.mean(axis=1))

variance=np.var(x)+np.var(y)+np.var(z)
sum(df.var(axis=1))
#variance is  0.0099534974238807503

#creat for looop that goes through 3AM-12AM and gets xyz values and means for each of them
import glob
list_of_files=glob.glob('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/*.csv')
c=0

#Loop through all files to get the summary statistic for each
mean=[]
ssq=[]
variance=[]
for file in list_of_files:
    columns=['time stamp','UTC time','accuracy','x','y','z']
    df=pd.read_csv(file,header=0,sep=',',names=columns)
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    x=df['x'].values
    y=df['y'].values
    z=df['z'].values
    c+=1
    avg=np.mean(df.mean(axis=0))
    var=sum(df.var(axis=0))
    sumofsq=sum(x**2)+sum(y**2)+sum(z**2)
    variance.append(var)
    mean.append(avg)
    ssq.append(sumofsq)

variance  
plt.plot(mean,"ko",linewidth=2,markersize=4);
plt.title('Mean')
plt.savefig("Mean.pdf")
plt.plot(variance,"ko",linewidth=2,markersize=4,label="Variance");
plt.title('Variance')
plt.savefig("Variance.pdf")
plt.plot(ssq,"ko",linewidth=2,markersize=4);
plt.title('Sum of Squares')
plt.savefig("Sum of Squares.pdf")
c
df.head()

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
#not finished


columns=['Questions','Answers']
df_ = pd.DataFrame(columns=columns)
df=pd.DataFrame(sleep,columns=columns)
pd.DataFrame.add()

#

os.getcwd()
#for i in range(3,24):
   # 2017-06-18 03_00_00
#############NOTES BELOW, ignore############
import csv

b=[1,2,3]
b
sum(b)
c=[("1,2,3")]
d=("1,6,3")
str(c)
c = c.replace(',', '')
numbers=map(float,'1,2,3'.split(','))#need to remove commas because cannot convert this to float
numbers=map(float,d.split(','))#converts string to list, removes commas, and sums
numbers
float(d)
type(d)
sum(numbers)
numbers=map(float,c.split(','))#

#
list1 = ['1', '2', '3']
str1 = ' '.join(list1)
str1

results = ['1', '2', '3']
results
results = list(map(int, results))
sum(results)


c#maybe print numbers that are only even, skips the commas
for i in c:
    print(float(i[4]))
    
sum(b)
#line is a string
from itertools import islice
xyz=[]


for line in open('C:/Users/Silvio/Documents/Python/v3dw1iq/accelerometer/2017-06-18 03_00_00.csv'):
    #print(line)
    line=line.rstrip()
    a=(line.split(",")[3:])
    xyz.append(a)
xyz
#main issue: transfer e's from data, and convert str to int or float
numbers=(map(float,xyz.split(',')))#convert to float
sum(numbers)#says float argument must be string/number, not list???
type(xyz)
sum(float(xyz[1])+float(xyz[2])
float(xyz[1])

    
values=df['x'].values
values
with open("C:\Users\Silvio\Documents\Python\v3dw1iq\accelerometer\2017-06-18 03_00_00") as f:
    i

ms = "a,b,c,d"
ms.split('-')[2:]

y=['Name1', '7.3', '6.9', '6.6', '6.6', '6.1', '6.4', '7.3\n']
y[-1] = y[-1].strip()
t = map(lambda s: s.strip(y), t)
print(y)

#start opening at row 
import io
with open('random.xlsx') as f:
    for i in xrange(3):
        f.next()
    for line in f:
        process(line)
xr