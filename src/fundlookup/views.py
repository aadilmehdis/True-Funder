from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Party, UserProfile, Vendor, Funder, PoliticalParty, Admin, Transaction
import requests
import json
import time
import geopy, sys
import os
import pandas
from geopy.geocoders import Nominatim, GoogleV3
import csv, json
from geojson import Feature, FeatureCollection, Point

def user_type(pk,name) :
    
    try :
        a = UserProfile.objects.get(user=pk).user_type
        print(a)
        print(a,name,"asdas")
    except UserProfile.DoesNotExist :
        a = None
        
    return a

def index(request):

    all_parties = Party.objects.all()
    all_parties1 = UserProfile.objects.filter(user_type='PP')
    context = {
        'all_parties'   : all_parties1,
        'user_type'     : user_type(request.user.pk, request.user)
    }
    # print(all_parties1)
    # context = {
    #     'all_parties': all_parties,
    #     'user_type' : user_type(request.user.pk)
    # }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):

    party = UserProfile.objects.get(pk=pk)
    transaction_history_url = "http://chacoins.eastus.cloudapp.azure.com/api?module=account&action=tokentx&address=%s" % (party.metamask_address)
    # transaction_history = json.loads(requests.get(transaction_history_url).text)['result']
    transaction_history = ""
    spent = 0
    received = 0
    spent = str(spent) + " CC"
    received = str(received) + " CC"

    context = {
        'party': party,
        'transaction_active': True,
        'transactions': transaction_history,
        'spent': spent,
        'received': received,
        'user_type' : user_type(request.user.pk, request.user),
    }
    return render(request, 'account/profile.html', context)
    # if user.user_type == 'PP':
    #     return render(request, 'account/profile.html', context)
    # elif user.user_type == '':
    #     pass
    # elif user.user_type == '':
    #     pass
    # elif user.user_type == '':
    #     pass

def transfer(request, pk=None):

    # party = Party.objects.get(pk=pk)
    party = UserProfile.objects.get(pk=pk)

    context = {
        'party': party,
        'transfer_active': True,
        'user_type' : user_type(request.user.pk),
    }

    
    party_profile = PoliticalParty.objects.get(user=party.user)
    if party_profile.enabled:
        return render(request, 'account/transfer.html', context)
    return redirect(profile, pk=party.pk)

def deposit(request, pk=None):

    # party = Party.objects.get(pk=pk)
    user = UserProfile.objects.get(pk=pk)
    context = {
        'user': user,
        'deposit_active': True,
        'user_type' : user_type(request.user.pk, request.user),
    }

    return render(request, 'account/deposit.html', context)

def pay(request, pk=None):

    vendor_types = ["(PB) Publicity", "(EV) Event", "(TR) Travel","(MC) Miscellaneous"]

    myparty = UserProfile.objects.get(pk=pk)
    party = Party.objects.all()
    context = {
        'vendor_types': vendor_types,
        'party': myparty,
        'pay_active': True,
        'user_type' : user_type(request.user.pk, request.user)
    }

    return render(request, 'account/pay.html', context)

def analytics(request, pk=None):
    get_loc()
    party = UserProfile.objects.get(pk=pk)
    values = [65, 59, 80, 81, 56, 55, 40]
    labels = ["January", "February", "March", "April", "May", "June", "July"]

    context = {
        'analytics_active': True,
        'values': values,
        'labels': labels,
        'party': party,
        'balance' : "1250 CC",
        'user_type' : user_type(request.user.pk, request.user)
    }

    return render(request, 'account/analytics.html', context)

def load_vendor(request):
    vendor_type = request.GET.get('vendor_type')
    vendors = Vendor.objects.filter(vendor_type=vendor_type)
    # vendors = Vendor.objects.filter(type=vendor_type).order_ascending
    return render(request, 'account/dropdown_vendor.html', {'vendors': vendors})


def get_loc():

    def get_latitude(x):
        return x.latitude

    def get_longitude(x):
        return x.longitude
    
    def get_area_name(x):
        return x.address

    geolocator = Nominatim(timeout=10)

    data = {'Area_Name':['Kerala', 'Hyderabad', 'Jaipur','Kerala']}
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