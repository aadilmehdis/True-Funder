from django.shortcuts import render
from django.http import HttpResponse
from .models import Party
import requests
import json
import time
import geopy, sys
import os
import pandas
from geopy.geocoders import Nominatim, GoogleV3
import csv, json
from geojson import Feature, FeatureCollection, Point

def index(request):
    print(request.user)
    print(request.user.pk)
    print(request.user.is_authenticated)
    all_parties = Party.objects.all()

    context = {
        'all_parties': all_parties
    }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):

    party = Party.objects.get(pk=pk)

    transaction_history_url = "http://chacoin.eastus.cloudapp.azure.com/api?module=account&action=tokentx&address=%s" % (party.address)
    # transaction_history = json.loads(requests.get(transaction_history_url).text)['result']
    transaction_history = ""
    spent = 0
    received = 0

    # for t in transaction_history:
    #     t['value'] = int(t['value']) / 1e18
    #
    #     if str(t['from']) == str(party.address).lower():
    #         spent += t['value']
    #         t['value'] =  "-" + str(t['value']) + " CC"
    #         t['state'] = True
    #     else:
    #         received += t['value']
    #         t['value'] =  "+" + str(t['value']) + " CC"
    #         t['state'] = False
    #     t['timeStamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(t['timeStamp'])))

    spent = str(spent) + " CC"
    received = str(received) + " CC"

    context = {
        'party': party,
        'transaction_active': True,
        'transactions': transaction_history,
        'spent': spent,
        'received': received
    }

    return render(request, 'account/profile.html', context)

def transfer(request, pk=None):

    party = Party.objects.get(pk=pk)
    context = {
        'party': party,
        'transfer_active': True,
    }

    return render(request, 'account/transfer.html', context)

def deposit(request, pk=None):

    party = Party.objects.get(pk=pk)
    context = {
        'party': party,
        'deposit_active': True,
    }

    return render(request, 'account/deposit.html', context)

def pay(request, pk=None):

    myparty = Party.objects.get(pk=pk)
    party = Party.objects.all()
    context = {
        'allparty': party,
        'party': myparty,
        'pay_active': True,
    }

    return render(request, 'account/pay.html', context)

def analytics(request, pk=None):
    get_loc()
    party = Party.objects.get(pk=pk)
    values = [65, 59, 80, 81, 56, 55, 40]
    labels = ["January", "February", "March", "April", "May", "June", "July"]

    context = {
        'analytics_active': True,
        'values': values,
        'labels': labels,
        'party': party,
        'balance' : "1250 CC"
    }

    return render(request, 'account/analytics.html', context)

def load_vendor(request):
    vendor_type = request.GET.get('vendor_type')
    print(vendor_type,"ada")
    vendors = Party.objects.filter(pk__lte=vendor_type)
    # vendors = Vendor.objects.filter(type=vendor_type).order_ascending
    return render(request, 'account/dropdown_vendor.html', {'vendors': vendors})


def get_loc():

    def get_latitude(x):
        return x.latitude

    def get_longitude(x):
        return x.longitude
    
    def get_area_name(x):
        return x.address

    geolocator = Nominatim(timeout=5)

    data = {'Area_Name':['Kerala', 'Hyderabad', 'Jaipur']}
    print(os.getcwd())
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
    with open("./fundlookup/static/map_data/GeoObs888.json", "w") as f:
        f.write('%s' % collection)