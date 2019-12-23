from django.shortcuts import render
from musics.models import Music
from musics.serializers import MusicSerializer
from rest_framework import viewsets

# Create your views here.
# Define CRUD function in modelviewset
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer