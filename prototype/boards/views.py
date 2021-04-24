from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Hello, World!')
    return render(request, 'homepage_simple.html')

# Create your views here.

def itineraryView(request):
    return render(request, 'itinerary.html')

def eventsView(request):
    return render(request, 'eventsmap.html')

def testView(request):
    return render(request, 'test.html')
