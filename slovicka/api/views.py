from rest_framework.response import Response
from rest_framework.decorators import api_view
from page.models import Dictionary
from .serializers import DictSerializer
@api_view(["GET"])
def getData(request):
    dicts = Dictionary.objects.all().filter(creator_id=request.user.id)
    person = {'name':"Egor",'age':19}
    ser = DictSerializer(dicts, many="True")
    return Response(ser.data)