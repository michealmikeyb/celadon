from django.shortcuts import render
from home.pages import pages

# Create your views here.

def landing(request):
    return render(request, 'home/landing.html')

def display_pages(request, page):
    return render(request, 'home/display_page.html', pages[page])
