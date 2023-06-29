from rest_framework import serializers
from page.models import Dictionary
class DictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dictionary
        fields = '__all__'

    