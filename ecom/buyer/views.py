from django.shortcuts import render

# Create your views here.
def buyer(request):
    return render(request,'buyer/buyer home.html')
