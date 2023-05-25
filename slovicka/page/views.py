from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser, User
# Create your views here.
from .models import *
def index(request):
    return render(request,'page/index.html',{
        'user': request.user,
        "registrated": not request.user == AnonymousUser(),
        "dictionarys": Dictionary.objects.all().filter(creator_id=request.user.id)
    })
def recent_dicts(request):
    a = Dictionary.objects.all().filter(creator_id=request.user.id).order_by('date').reverse()
    b = []
    for obj in a:
        b.append(obj.name)
    return render(request,'page/list.html',{
        "dicts":b
    })