from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
   # return HttpResponse("Hello World")
   return render(request,'game/index.html')

def gallery(request):
   # return HttpResponse("Hello World")
   return render(request,'game/gallery.html')

def chess(request):
   # return HttpResponse("Hello World")
   return render(request,'game/home.html')

def quiz(request):
   # return HttpResponse("Hello World")
   return render(request,'game/trivia.html')