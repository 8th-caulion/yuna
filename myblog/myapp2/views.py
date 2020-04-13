from django.shortcuts import render

# Create your views here.


def myfriends(request):
    return render(request, 'myfriends.html')
