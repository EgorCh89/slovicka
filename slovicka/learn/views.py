from django.shortcuts import render
from page.models import *
# Create your views here.
# Create your views here.
def index(request, name):
    dict = Dictionary.objects.all().filter(creator_id=request.user.id, name=name)
    dict = dict[0]

    pairs = Pair.objects.all().filter(dict=dict)

    return render(request,'learn/index.html',{
        'dict':dict,
        'pairs':pairs
    })
def index_all(request):
    dict = Dictionary.objects.all().filter(creator_id=request.user.id)
    return render(request,'learn/list.html',{
        'dicts':dict,
    })

def cards(request, name):
    dict = Dictionary.objects.all().filter(creator_id=request.user.id, name=name)
    dict = dict[0]

    pairs = Pair.objects.all().filter(dict=dict)

    return render(request,'learn/cards.html',{
        'dict':dict,
        'pairs':pairs
    })