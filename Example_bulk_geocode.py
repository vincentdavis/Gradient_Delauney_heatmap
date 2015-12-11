# Example

# This is to add the geocode file for me (vincent) you might need somthing different or nothing
import sys
sys.path.append("/Users/vincentdavis/Gradient_Delauney_heatmap")


import csv
from pygeocoder import Geocoder
import time
import random
import geocode

SAMPLESIZE = 500

def ramdom_rows(fname, rowcount):
    '''
    Randomly read rows
    This is not perfect some of the rows selected are though out later
    '''
    rows = []
    for i, row in enumerate(csv.DictReader(open(fname))):
        if (int(row["TOTACTVAL"]) > 50000 and row["STTSTRC"].strip(' ') == 'RESID' and row["PRPCTYNAM"].strip(' ') == 'ARVADA' and 
        int(row["TOTACTIMPV"]) > 50000):
            #print('V', row["VALACT"])
            rows.append(i)
    return random.sample(rows, rowcount)

readrows = ramdom_rows("Data2009.csv", SAMPLESIZE)

print('Len readrows', len(readrows))


# open samle data with per row dictionary
data = csv.DictReader(open("Data2009.csv"))


# GeoCode from address
latlon = []
propvalue = []
sqft = []
rowcount = 0
for row in data:
    if rowcount in readrows:
        results = geocode.jeffco(row['SCH'])
        # this will result in lost rows
        if results not in latlon and results is not None: # make sure there are no duplicats
            if len(latlon) % 100 == 0:
                print('RowCount', rowcount, 'Val', row["TOTACTVAL"], "SCH",  row["SCH"], "len(latlon)", len(latlon))
            propvalue.append(int(row["TOTACTVAL"]))
            sqft.append(int(row["STTGRSAREA"]))
            latlon.append(results)
        time.sleep(.5)
    rowcount += 1


pickle.dump( latlon, open( "Example_latlon.p", "wb" ) )
pickle.dump( propvalue, open( "Example_propvalue4.p", "wb" ) )
pickle.dump( sqft, open( "Example_sqft4.p", "wb" ) )


points = numpy.asarray(latlon)
propvalue = numpy.asarray(propvalue)
sqft = numpy.asarray(sqft)

print("(Max, Min) Prop Value", propvalue.max, propvalue.min(), "(Max Min) sqft", sqft.max(), sqft.min())