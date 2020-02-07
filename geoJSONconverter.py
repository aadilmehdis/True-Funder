import geopy, sys
import pandas
from geopy.geocoders import Nominatim, GoogleV3
# versions used: geopy 1.10.0, pandas 0.16.2, python 2.7.8

import csv, json
from geojson import Feature, FeatureCollection, Point


inputfile=str(sys.argv[1])
namecolumn=str(sys.argv[2])

def main():

    def get_latitude(x):
        return x.latitude

    def get_longitude(x):
        return x.longitude
    
    def get_area_name(x):
        return x.address

    geolocator = Nominatim(timeout=5)

    data = {'Area_Name':['Gujarat', 'Hyderabad', 'Jaipur']}
    io = pandas.DataFrame(data)

    geolocate_column = io['Area_Name'].apply(geolocator.geocode)
    io['latitude'] = geolocate_column.apply(get_latitude)
    io['longitude'] = geolocate_column.apply(get_longitude)
    io.to_csv('geocoding-output1.csv')

    features = []
    with open('geocoding-output1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print(reader)
        i = 0
        for _, Area_Name, latitude, longitude in reader:
            if i==0:
                i = 1
                continue
            latitude, longitude = map(float, (latitude, longitude))
            features.append(
                Feature(
                    geometry = Point((longitude, latitude)),
                    properties = {
                    }
                )
            )

    collection = FeatureCollection(features)
    with open("GeoObs.json", "w") as f:
        f.write('%s' % collection)

if __name__ == '__main__':
    main()

