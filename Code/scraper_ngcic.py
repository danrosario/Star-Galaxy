# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:31:13 2016

@author: suryo
"""

import mechanize
import os
import csv

def extractData (content):
    S = content
    where = S.find('Right Ascension (2000)')
    ra = S[where+64:where+77]
    ra = ra.replace('h', '')
    ra = ra.replace('m', '')
    ra = ra.replace('s', '')

    where = S.find('Declination (2000)')
    dec = S[where+60:where+77]
    dec = dec.replace('&ordm;', '')
    dec = dec.replace("'", '')
    dec = dec.replace('"', '')
    
    where = S.find('Object Size')
    x = S[where+53:where+61]
    x = x.replace('&ordm;', '')
    x = x.replace("'", '')
    x = x.replace('"', '')
    
    #print x
    try:
        x,y = x.split("X")
    except:
        x = None
        y = None
    
    return ra, dec, x, y

path = '/home/suryo/MyStuff/MyDevelopment/AstroSSDS/code/coordinates/ngc/'
files_list = os.listdir(path)
#print len(files_list)

for i in range (len(files_list)+1,7843):
    
    print "\nObject = NGC ", str(i)
    
    while True:
        try:
            br=mechanize.Browser()
            br.set_handle_robots(False)
            print "Loading form."
            br.open("http://ngcicproject.org/pubdb.htm")
            print "Form loaded."
            
            br.select_form(nr = 0)
            br["ngcicobject"] = "n" + str(i)
            res = br.submit()
            print "Request submitted. Waiting for response."
            content = res.read()

            ra, dec, x, y = extractData(content)
            break
    
        except:
            print "Failed."
            continue
              
    print "RA = ", ra
    print "DEC = ", dec
    print "x = ", x
    print "y = ", y
    
    coord = []
    coord.append(str(ra))
    coord.append(str(dec))
    coord.append(str(x))
    coord.append(str(y))
    
    fileName = path+str(i)+'.csv'
    #np.savetxt(fileName,dataMatrix,delimiter=',',newline='\n')
    writer = csv.writer(open(fileName, 'w'))
    writer.writerow(coord)


path = '/home/suryo/MyStuff/MyDevelopment/AstroSSDS/code/coordinates/ic/'
files_list = os.listdir(path)
#print len(files_list)

for i in range (len(files_list)+1,5390):
    
    print "\nObject = IC ", str(i)
    
    while True:
        try:
            br=mechanize.Browser()
            br.set_handle_robots(False)
            print "Loading form."
            br.open("http://ngcicproject.org/pubdb.htm")
            print "Form loaded."
            
            br.select_form(nr = 0)
            br["ngcicobject"] = "i" + str(i)
            res = br.submit()
            print "Request submitted. Waiting for response."
            content = res.read()

            ra, dec, x, y = extractData(content)
            break
    
        except:
            print "Failed."
            continue
              
    print "RA = ", ra
    print "DEC = ", dec
    print "x = ", x
    print "y = ", y
    
    coord = []
    coord.append(str(ra))
    coord.append(str(dec))
    coord.append(str(x))
    coord.append(str(y))
    
    fileName = path+str(i)+'.csv'
    #np.savetxt(fileName,dataMatrix,delimiter=',',newline='\n')
    writer = csv.writer(open(fileName, 'w'))
    writer.writerow(coord)