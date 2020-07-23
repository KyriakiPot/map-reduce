#!/usr/bin/env python3

import json
import sys

#anoigma arxeiou
for line in sys.stdin:
    authors = []
    try:
        #xwrismos tis grammis se 2 meri
        data1,data2 = line.split('"authors": [')
        #xwrismos tou deuterou merous gia na meinoun mono oi siggrafeis
        d = data2.split("],")
        #xwrismos apothikeusi twn authors se pinaka
        authors = d[0].split(',')
        for idex, value in enumerate(authors):
            #dimiourgia kleidiou me basi tous authors kai tin thesi pou vriskontai ston pinaka
            key = value + (',') + str(idex + 1) 
            #exodos tou mapper kai eisodos tou reducer
            print ('%s\t%s' % (key, 1))
        
    except ValueError: 
        continue
        
        


