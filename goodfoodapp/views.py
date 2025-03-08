from django.shortcuts import render

# Create your views here.
def home_page(req):
    return render(req,'testApp/index.html')

def home_view(req):
    return render(req,'testApp/home.html')    