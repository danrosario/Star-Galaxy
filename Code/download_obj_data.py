# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:26:01 2016

@author: suryo
"""
import mechanize
from BeautifulSoup import BeautifulSoup
import re
import csv
import urllib
import os

total = 3025
count = 0
present_files = os.listdir('data/')
print 'THE FILES WHICH ARE ALREADY PRESENT:'
print present_files

for i in range (0,len(present_files)):
    ret, temp = (None, re.split(r'\.', present_files[i].strip()))
    present_files[i] = temp[0]
#print present_files        

with open('ESO_Red.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        current_coords = []
        ret, current_coords = (None, re.split(r' *', row[0].strip()))
        
        print ''
        print 'OBJECT =',current_coords[0]
        print 'DIMENSIONS =',current_coords[7], "X", current_coords[8]
        count+=1
        print 'DOWNLOADING OBJECT '+str(count) +'/' +str(total)
        
        if current_coords[0] in present_files:
            print "This object's catalog is already downloaded. Not downloading again."
            continue
        
        while True:
            try:
                br=mechanize.Browser()
                br.set_handle_robots(False)
                print "Loading form."
                br.open("http://www-wfau.roe.ac.uk/sss/obj.html")
                print "Form loaded."
            
                br.select_form(nr = 0)
                #print br
                
                br["coords"] = current_coords[1] + " " + current_coords[2] + " " + current_coords[3] + " " + current_coords[4] + " " + current_coords[5] + " " +current_coords[6]
                br["xsize"] = current_coords[7]
                br["ysize"] = current_coords[8]
                br["equinox"] = ['2']               #DON'T CHANGE THIS
                br["waveband"] = ['4']              #CHANGE THIS ACCORDING TO SURVEY
                br["purge"] = ['0']                 #DON'T CHANGE THIS
                br["subset"] = ['0']                #DON'T CHANGE THIS
                br['blend'] = ['2']                 #DON'T CHANGE THIS
                br["quality"] = "99999999"          #DON'T CHANGE THIS

                print "Submitting request."                
                res = br.submit()        
                print "Request submitted. Waiting for response."
        
                content = res.read()
        
                #WHEN THE ASCII CATALOG IS NOT COMPRESSED
                if ("The object catalogue is" in content) == True:
                    where = content.find('The object catalogue is')
                    #print where
                    index = where
                    c = content[index]
            
                    while (c != "'"):
                        index+=1
                        c = content[index]
            
                    index += 1
                    c = content[index]
                    url = ''
            
                    while (c!="'"):
                        url+=c
                        c = content[index]
                        index += 1
            
                    url = url[1:]
                    
                    print 'The URL is',url

                    print "Downloading ASCII file using urllib."
                    urllib.urlretrieve(url, 'data/' + current_coords[0]+".ascii")
                    print "Download complete."
                
                #WHEN THE ASCII CATALOG IS COMPRESSED
                elif ("The gzipped object catalogue is" in content) == True:
                    where = content.find('The gzipped object catalogue is')
                    #print where
                    index = where
                    c = content[index]
            
                    while (c != "'"):
                        index+=1
                        c = content[index]
            
                    index += 1
                    c = content[index]
                    url = ''
            
                    while (c!="'"):
                        url+=c
                        c = content[index]
                        index += 1
            
                    url = url[1:]
                    
                    print 'The URL is',url

                    print "Downloading .gz file using urllib."
                    urllib.urlretrieve(url, 'data/' + current_coords[0]+".ascii.gz")
                    print "Download complete."

                
                else:
                    print 'No link for this object.'
            
                #soup = BeautifulSoup(content)
                #print soup.prettify()
                br.close()
                break
    
            except:
                print "Failed."
                continue