from backend.models import User, Jurado, Organitation, Calification, Category, Vote
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, JuradoSerializers, OrganitationSerializers, CategorySerializers, CalificationSerializers, VoteSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class JuradoViewSet(viewsets.ModelViewSet):
    queryset = Jurado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JuradoSerializers


class OrganitationViewSet(viewsets.ModelViewSet):
    queryset = Organitation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganitationSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializers


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VoteSerializers


class CalificationViewSet(viewsets.ModelViewSet):
    queryset = Calification.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CalificationSerializers
