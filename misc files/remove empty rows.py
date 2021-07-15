# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:03:48 2020

@author: Kislay
"""
import numpy as np
import csv

ins = open( "D:/data/your_file.txt", "r" )
    
array = []
for line in ins:
    line = line.rstrip('\n')
    array.append( line )
ins.close()
data=[[]]

final=[[0]*134]*5000
for item in array :
         data.append(item.split(','))
data.pop(0)         
data=np.array(data)
final=np.array(final)
for i in range(4920):
    for j in range(1,18):
        final[i][0]=data[i][0]
        final[i][int(data[i][j])]=1
print(final)





with open("D:/data/new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(final)