from ip2geotools.databases.noncommercial import Ipstack
import gmplot

# read the ip list
ip_list = []
geo_list = []
with open('data/ip_list.txt', 'r') as f:
    for line in f.readlines():
        ip = line.rstrip('\n')
        ip_list.append(ip)
        response = Ipstack.get(ip, api_key='e3a22cebedfd1a296677b0e532******')   # (your Ipstack API key here)
        geo_list.append((response.latitude, response.longitude))

# Create the map plotter:
apikey = 'AIzaSyDECZHeOZkzPt1NT98b0rpPLQwDi******'  # (your Google API key here)
gmap = gmplot.GoogleMapPlotter(geo_list[0][0], geo_list[0][1], 11, apikey=apikey)

# Mark yourself:
gmap.marker(geo_list[0][0], geo_list[0][1], color='cornflowerblue')

# Highlight a set of users:
attractions_lats, attractions_lngs = zip(*geo_list[0::2])
gmap.scatter(attractions_lats, attractions_lngs, color='blue', size=100, marker=False)
attractions_lats, attractions_lngs = zip(*geo_list[1::2])
gmap.scatter(attractions_lats, attractions_lngs, color='red', size=100, marker=False)

# Draw the map:
gmap.draw('map.html')
