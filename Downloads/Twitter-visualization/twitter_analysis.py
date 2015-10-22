# import modules
import tweepy
import csv
import json
import geopy
from collections import Counter
from geopy import geocoders  
from urllib2 import urlopen

# Consumer keys and access tokens, used for OAuth
consumer_key = 'XXXX XXXX XXXX XXXX'
consumer_secret = 'XXXX XXXX XXXX XXXX'
access_token = 'XXXX XXXX XXXX XXXX'
access_token_secret = 'XXXX XXXX XXXX XXXX'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# to get longitude and latitude
gn = geocoders.GoogleV3()

# opening csv file in writing mode
csvFile = open('result.csv', 'wb')

#Use csv Writer
csvWriter = csv.writer(csvFile)

	
#Coords = dict()
#Place = dict()
#PlaceCoords = dict()
#XY = []
#list = []
#count1=0

# google api function to get country from longitude and latitude
def getplace(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    return country
	
# search query to get results
results=api.search(	q="#mh17",
					count=1000,
					#rpp=10000,
					since="2014-07-20",
                    until="2014-07-25",
					#geocode="39.95256,-75.164,4mi",
                    result_type="recent",
                    include_entities=True,
                    lang="en")
# writing header row to csv file
print csvWriter.writerow(["Timestamp", "Status", "Place", "Longitude", "Latitude", "Country"])

# iterate the output of results
for result in results:
		if result.user.location.encode('utf-8')!='':
			try:
				if gn.geocode(result.user.location.encode('utf-8')):
					place, (lat, lng) = gn.geocode(result.user.location.encode('utf-8'),timeout=40000)
					print(getplace(lat, lng))
					print csvWriter.writerow([result.created_at, result.text.encode('utf-8'),place.encode('utf-8'),lat,lng,getplace(lat, lng)])
				else :
					print "none1"
			# exception caught
			except geopy.exc.GeocoderTimedOut:
				print "service timed out"
		else:
			print "none"
			
		#result.created_at, result.text.encode('utf-8'), result.user.location, result.coordinates, result.user.geo_enabled, result.source.encode('utf-8')])
		#print "status=",result.text.encode('utf-8'),"\n"
		#, "location=",result.user.location,"\n", result.coordinates, "\n","geo enabled:",result.user.geo_enabled, "\n",result.source.encode('utf-8')
		#print result
		#if result.user.location.encode('utf-8')!='':
			#list.append(result.user.location.encode('utf-8'))
#print list
#counts = Counter(list)
#print counts
		#print "timezone",result.user.time_zone
		#print "geo:",result.geo
		#if result.user.location.find('worldwide'):
			#count1=count1+1	
#print count1
		#result.user.screen_name , "\n",result.user.name
		#if result.user.geo_enabled:
			#try:
			#	Coords.update(result.coordinates)
			#	XY 	= (Coords.get('coordinates')) 
			#	print "X: ", XY[0]
			#	print "Y: ", XY[1]
			#except:
			#	Place.update(result.place)
			#	PlaceCoords.update(Place['bounding_box'])
			#	Box = PlaceCoords['coordinates'][0]
			#	XY = [(Box[0][0])+Box[2][0]/2, Box[0][1]+Box[2][1]/2]
			#	print XY[0]
			#	print XY[1]
			#pass
		#else:
			#print "none"