from django.shortcuts import render
from django.http import HttpResponse
from .models import Party

def index(request):

    all_parties = Party.objects.all()
    for p in all_parties:
        print(p.symbol)
    context = {
        'all_parties': all_parties
    }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):
    print(request)
    print(pk)
    party = Party.objects.get(pk=pk)

    context = {
        'party': party,
        'transaction_active': True,
        'transactions': [],
    }

    return render(request, 'account/profile.html', context)

def pay(request, pk=None):

    party = Party.objects.get(pk=pk)
    context = {
        'party': party,
        'pay_active': True,
    }

    return render(request, 'account/pay.html', context)
