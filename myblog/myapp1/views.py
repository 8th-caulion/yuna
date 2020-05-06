from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main.html')


def mymbti(request):
    return render(request, 'mymbti.html')


def myreport(request):
    return render(request, 'myreport.html')


def mychildhood(request):
    return render(request, 'mychildhood.html')
