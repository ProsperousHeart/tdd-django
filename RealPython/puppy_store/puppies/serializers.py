from rest_framework import serializers
from .models import Puppy


# http://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')