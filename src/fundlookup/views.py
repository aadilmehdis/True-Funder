from django.shortcuts import render
from django.http import HttpResponse
from .models import Party
import requests

def index(request):

    all_parties = Party.objects.all()
    for p in all_parties:
        print(p.symbol)
    context = {
        'all_parties': all_parties
    }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
        # print(user.username)
    else:
        user = request.user


    c = requests.get("http://chacoin.eastus.cloudapp.azure.com/api?module=account&action=tokentx&address=0xf2838B47B20a0c5e7dA09F7C6f248584e75cAeeA&contractaddress=0x729703741512932bb12484372289e8f0bb7f2556")
    # d = requests.get("http://chacoin.eastus.cloudapp.azure.com/api?module=account&action=txlist&address=0x729703741512932bb12484372289e8f0bb7f2556")

    print(c)
    print(d)

    context = {
        'transaction_active': True,
        'party_name': '',
        'party_image_path': '',
        'transactions': [],
    }

    return render(request, 'account/profile.html', context)

def pay(request):

    context = {
        'pay_active': True,
    }

    return render(request, 'account/pay.html', context)
