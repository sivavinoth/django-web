from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import movie
def homes(request):
    
    searchterm =request.GET.get("searchMovie")
    if searchterm :
        movies =movie.objects.filter(title__icontains =searchterm)
    else:
        
        movies =movie.objects.all()
    return render(request, 'home.html',{'searchterm':searchterm,'movies':movies})

def signup(request):
    email = request.GET.get("email")
    return render(request,'signup.html',{'email':email})


def about(request):
    return HttpResponse("<h1>This is About page<h2>")



















