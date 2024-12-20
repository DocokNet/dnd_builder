from rest_framework import serializers
from .models import Races, Background, Classes, Class_skills, Current_class_info, Player

class RacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Races
        fields = ['id', 'name', 'pros', 'cons', 'description']

class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ['id', 'name', 'background_skills', 'languages', 'instruments_prof', 'background_gear']

#class ArchetypesSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Archetypes
#        fields = ['id', 'archetype_name']

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'class_name', 'hp_dice']

class ClassSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_skills
        fields = ['id', 'name', 'class_id', 'description']

#class ArchetypeSkillsSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Archetype_skills
#        fields = ['id', 'name', 'archetype_id']

class CurrentClassInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current_class_info
        fields = ['id', 'class_id']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['list_id', 'character_name', 'level', 'class_table', 'race_id', 'background_id', 'alignment', 'hit_points', 'experience', 'stats', 'skills', 'gear']