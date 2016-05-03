# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:49:48 2016

@author: suryo
"""

import numpy as np
import csv
import re
import urllib

def coord_subset(low, high, coord,name):

    path = '/home/suryo/MyStuff/MyDevelopment/AstroSSDS/code/coordinates/passbands/'
    outfile = path + name + '.csv' 
    name_coord = []
    count = 0
    for row in coord:
        if (row[1] != 'None'):
            
            ret, dec = (None, re.split(r' ', row[2].strip()))
            """
            print dec
            print dec[0]
            print dec[1]
            print dec[2]
            """
            deg = float(dec[0])
        
            if (low <= deg) and (deg <=high):
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                temp.append(row[3])
                temp.append(row[4])
                
                print temp[0]
                print temp[3]
                if(temp[3] != 'None'):
                    print float(temp[3].strip())
                    
                if (temp[3] == 'None') or (float(temp[3]) < 7):
                    temp[3] = '7.0'
                    
                if (temp[4] == 'None') or (float(temp[4]) < 7):
                    temp[4] = '7.0'
                
                name_coord.append(temp)
                print temp
                count += 1
                print count
                print ''
                
    np.savetxt(outfile,name_coord,fmt='%s')
            
coord = []
count = 0
with open("/home/suryo/MyStuff/MyDevelopment/AstroSSDS/code/coordinates/coordinates.csv",'rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        count+=1
        coord.append(row)
        if(len(row) < 5):
            print count
        
#print coord
#print len(coord)

c = '1.0'
print float(c.strip())
coord_subset(2,90,coord,'POSS_2_Infrared')

count = 0
coordinates = []
with open('/home/suryo/MyStuff/MyDevelopment/AstroSSDS/code/coordinates/passbands/POSS_2_Infrared.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        coordinates.append(row)
        count+=1
print count
print len(coordinates)