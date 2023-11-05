from rest_framework import serializers
from .models import Verb

class VerbSerializer(serializers.ModelSerializer):
    class Meta:
        model=Verb
        fields='__all__'
