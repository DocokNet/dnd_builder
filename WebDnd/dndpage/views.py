from django.shortcuts import render
from rest_framework import generics
from .models import (Races, 
                     Background, 
                     #Archetypes, 
                     Classes, 
                     Class_skills, 
                     #Archetype_skills,
                     Current_class_info, 
                     Player)
from .serializers import (
    RacesSerializer,
    BackgroundSerializer,
    #ArchetypesSerializer,
    ClassesSerializer,
    ClassSkillsSerializer,
    #ArchetypeSkillsSerializer,
    CurrentClassInfoSerializer,
    PlayerSerializer
)

class RacesListCreateView(generics.ListCreateAPIView):
    queryset = Races.objects.all()
    serializer_class = RacesSerializer

class BackgroundListCreateView(generics.ListCreateAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer

#class ArchetypesListCreateView(generics.ListCreateAPIView):
#    queryset = Archetypes.objects.all()
#    serializer_class = ArchetypesSerializer

class ClassesListCreateView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class ClassSkillsListCreateView(generics.ListCreateAPIView):
    queryset = Class_skills.objects.all()
    serializer_class = ClassSkillsSerializer

#class ArchetypeSkillsListCreateView(generics.ListCreateAPIView):
#    queryset = Archetype_skills.objects.all()
#    serializer_class = ArchetypeSkillsSerializer

class CurrentClassInfoListCreateView(generics.ListCreateAPIView):
    queryset = Current_class_info.objects.all()
    serializer_class = CurrentClassInfoSerializer

class PlayerListCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

def maindndpage(request):
    return render(request, "dndpage/main_dnd_page.html",)


def lvdndpage(request):
    lv = [i + 1 for i in range(20)]
    return render(request, "dndpage/lv_dnd_page.html", {"lv": lv})

def geardndpage(request):
    gear = [
        {"name": "item1", "description": "item1 description", "quantity" : 1},
        {"name": "item2", "description": "item2 description", "quantity" : 1},
        {"name": "item3", "description": "item3 description", "quantity" : 1},
        {"name": "item4", "description": "item4 description", "quantity" : 1},
        {"name": "item5", "description": "item5 description", "quantity" : 1},
    ]
    return render(request, "dndpage/gear_dnd_page.html", {"gear": gear})


def infodndpage(request):
    return render(request, "dndpage/player_info_dnd_page.html")