"""
URL configuration for WebDnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dndpage import views
from dndpage.views import (
    RacesListCreateView,
    BackgroundListCreateView,
    #ArchetypesListCreateView,
    ClassesListCreateView,
    ClassSkillsListCreateView,
    #ArchetypeSkillsListCreateView,
    CurrentClassInfoListCreateView,
    PlayerListCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dndpage/', views.maindndpage),
    path('dndpage/lv/', views.lvdndpage),
    path('dndpage/gear/', views.geardndpage),
    path('dndpage/info/', views.infodndpage),
    path('api/races/', RacesListCreateView.as_view(), name='races-list-create'),
    path('api/backgrounds/', BackgroundListCreateView.as_view(), name='backgrounds-list-create'),
    #path('api/archetypes/', ArchetypesListCreateView.as_view(), name='archetypes-list-create'),
    path('api/classes/', ClassesListCreateView.as_view(), name='classes-list-create'),
    path('api/class-skills/', ClassSkillsListCreateView.as_view(), name='class-skills-list-create'),
    #path('api/archetype-skills/', ArchetypeSkillsListCreateView.as_view(), name='archetype-skills-list-create'),
    path('api/current-class-info/', CurrentClassInfoListCreateView.as_view(), name='current-class-info-list-create'),
    path('api/player/', PlayerListCreateView.as_view(), name='players-list-create'),
]
