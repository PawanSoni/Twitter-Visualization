# import csv module
import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# open and read the csv file into memory
file = open('result.csv')
reader = csv.reader(file)

# iterate through the lines and print them to stdout
# the csv module returns us a list of lists and we
# simply iterate through it
#for line in reader:
#	print line[3]

reader.next() #skip header
countries = [row[5] for row in reader]
# create dictionary named data
data={}

#sum=count number of tweets
sum=0
for (k,v) in Counter(countries).iteritems():
	sum=sum+v
	print "%s:%d" % (k, v)
	data[k] = v
#print data
#print "Total Number of Tweets", sum

#lists
temp = []
dictList = []

for key, value in data.iteritems():
    temp = [key,value]
    dictList.append(temp)
#print dictList

# chart plot and show
N = len( data )
x = np.arange(0, N)
y = [ num for [s,num] in dictList ]
labels = [ s for [s,num] in dictList ]
width = 1
bar1 = plt.bar( x, y, width, color="y" )
plt.ylabel( 'Number of Tweets for Query = #mh17' )
plt.title("Chart Between Countries And Number of Tweets for a Query (Total Tweets=%d)"%sum)
plt.xlabel("Countries")
plt.xticks(x+ width/2.0, labels,fontsize=9 )
plt.show()