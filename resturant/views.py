from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'resturant/index.html')

def menu(request):
    return render(request, 'resturant/menu.html')