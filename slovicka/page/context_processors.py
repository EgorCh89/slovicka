from .models  import Dictionary
from django.contrib.auth.models import AnonymousUser

def add_variable_to_context(request):
    if request.user:
        return {
            'myDictionaries': Dictionary.objects.all().filter(creator_id=request.user.id)[0:10],
            "registrated": not request.user == AnonymousUser(),
        }