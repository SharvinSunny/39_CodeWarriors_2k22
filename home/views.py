from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Homepage.html')
   #return HttpResponse("this is homepage")

def payment(request):
    return render(request, 'payment.html')

def regstray(request):
    return render(request, 'regstray.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')