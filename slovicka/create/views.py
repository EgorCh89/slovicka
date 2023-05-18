from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponsePermanentRedirect

import datetime
from  page.models import Dictionary, Pair
class NewDictForm(forms.Form):
    name = forms.CharField(label="Name",max_length=65)
    public = forms.BooleanField(label="public",required=False)



# Create your views here.
def index(request):
    return render(request,'create/index.html')

def create_new(request):
    if request.method == "POST":
        form = NewDictForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            for obj in Dictionary.objects.all().filter(creator_id=request.user.id):
                if obj.name == name:
                    message = "this title is taken"
                    return render(request,'create/new.html',{
                        'form': NewDictForm(request.POST),
                        "message":[message]
                    })
            pub = form.cleaned_data.get('public')
            dict = Dictionary(name=name,date=datetime.datetime.now(), public=pub,creator_id=request.user.id)
            dict.save()
            return HttpResponsePermanentRedirect(f'{name}/edit')
        else:
            return render(request,'create/new.html',{
            'form': NewDictForm(request.POST),
            })
    if request.method == "GET":
        return render(request,'create/new.html',{
            'form': NewDictForm(),
        })
    
def edit(request,name):

    dict = Dictionary.objects.all().filter(creator_id=request.user.id,name=name)
    if request.method == "GET":
        print(Pair.objects.all().filter(dict=dict[0]))
        return render(request,'create/edit.html',{
            "dict": dict[0],
            "pairs":Pair.objects.all().filter(dict=dict[0]).values()
        })
    if request.method == "POST":
        form = request.POST
        print(form)
        return render(request,'create/edit.html',{
            "dict": dict[0],
            "pairs":Pair.objects.all().filter(dict=dict[0]).values()
        })
