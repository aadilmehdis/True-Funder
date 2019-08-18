from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {


    }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
        # print(user.username)
    else:
        user = request.user

    context = {
        'party_name': '',
        'party_image_path': '',
        'transactions': [],
    }

    return render(request, 'account/profile.html', context)
