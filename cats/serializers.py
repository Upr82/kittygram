from rest_framework import serializers

from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year')


class CatSerializerFull(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
