from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser, User
# Create your views here.

def index(request):
    if request.user != AnonymousUser():
        print(request.user.id)
    return render(request,'page/index.html',{
        'user': request.user,
        "registrated": not request.user == AnonymousUser(),
    })