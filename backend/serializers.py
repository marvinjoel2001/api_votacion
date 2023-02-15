from rest_framework import serializers
from .models import User, Jurado, Organitation, Category, Calification, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class JuradoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jurado
        fields = '__all__'


class OrganitationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organitation
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class CalificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Calification
        fields = '__all__'
