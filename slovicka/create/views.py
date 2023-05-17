from django.shortcuts import render
from django import forms
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
            name = form.changed_data["name"]
            pub = form.changed_data["publi"]
            dict = Dictionary(name=name,date=datetime.datetime.now(), public=pub,creator_id=request.session.user.id)
            print(request.session.user.id)
            return render (request,f"/{name}/edit/",{
                # and object of dict
            })
        else:
            return render(request,'create/new.html',{
            'form': NewDictForm(request.POST),
            })
    if request.method == "GET":
        return render(request,'create/new.html',{
            'form': NewDictForm(),
        })
def edit(request,name):
    if request.method == "GET":
        return None
