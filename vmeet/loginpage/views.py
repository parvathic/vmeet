from django.shortcuts import render, HttpResponse

# Create your views here.
def loginpage(request):
    username = ['parvathic', 'user2']
    password = ['12345', 'hello']
    args = {'key': password}
    return render(request, 'loginpage/home.html', args)