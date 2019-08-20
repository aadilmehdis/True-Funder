from django.shortcuts import render
from django.http import HttpResponse
from .models import Party
import requests
import json
import time
def index(request):

    all_parties = Party.objects.all()

    context = {
        'all_parties': all_parties
    }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):

    party = Party.objects.get(pk=pk)

    transaction_history_url = "http://chacoin.eastus.cloudapp.azure.com/api?module=account&action=tokentx&address=%s" % (party.address)
    transaction_history = json.loads(requests.get(transaction_history_url).text)['result']
    spent = 0
    received = 0

    for t in transaction_history:
        t['value'] = int(t['value']) / 1e18

        if str(t['from']) == str(party.address).lower():
            spent += t['value']
            t['value'] =  "-" + str(t['value']) + " CC"
            t['state'] = True
        else:
            received += t['value']
            t['value'] =  "+" + str(t['value']) + " CC"
            t['state'] = False
        t['timeStamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(t['timeStamp'])))

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

def pay(request, pk=None):

    party = Party.objects.get(pk=pk)
    context = {
        'party': party,
        'pay_active': True,
    }

    return render(request, 'account/pay.html', context)
