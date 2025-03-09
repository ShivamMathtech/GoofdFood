from django.shortcuts import render

# Create your views here.
def home_page(req):
    return render(req,'testApp/index.html')

def home_view(req):
    return render(req,'testApp/home.html')  

def about_view(req):
    return render(req,'testApp/about.html')
def location_view(req):
    return render(req,'testApp/location.html')    

def contact_view(req):
    return render(req,'testApp/contact.html')