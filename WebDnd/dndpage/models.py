from django.db import models
from jsonfield import JSONField

class Races(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    pros = models.JSONField(default=dict())
    cons = models.JSONField(default=dict())
    description = models.CharField(max_length=1000)

    @classmethod
    def parseRaces(self):
        data = list(self.objects.all())
        prepared_data  = list()
        dicti = dict()
        for i in data:
            dicti["id"] = i.id
            dicti["name"] = i.name
            dicti["pros"] = i.pros
            dicti["cons"] = i.cons
            dicti["description"] = i.description
            prepared_data.append(dicti)
            dicti = dict()            
        return prepared_data

    def __str__(self):
        return self.name

class Background(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    background_skills = models.JSONField(default=list())
    languages = models.JSONField(default=list())
    instruments_prof = models.JSONField(default=list())
    background_gear = models.JSONField(default=list())

    @classmethod
    def parseBackground(self):
        data = list(self.objects.all())
        prepared_data  = list()
        dicti = dict()
        for i in data:
            dicti["id"] = i.id
            dicti["name"] = i.name
            dicti["background_skills"] = i.background_skills
            dicti["languages"] = i.languages
            dicti["instruments_prof"] = i.instruments_prof
            dicti["background_gear"] = i.background_gear
            prepared_data.append(dicti)
            dicti = dict()            
        return prepared_data

    def __str__(self):
        return self.name

#class Archetypes(models.Model):
#    id = models.AutoField(primary_key=True)
#    archetype_name = models.CharField(max_length=30)
#
#    def __str__(self):
#        return self.archetype_name

class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=20)
    hp_dice = models.CharField(max_length=10)

    @classmethod
    def parseClasses(self):
        data = list(self.objects.all())
        prepared_data  = list()
        dicti = dict()
        for i in data:
            dicti["id"] = i.id
            dicti["class_name"] = i.class_name
            dicti["hp_dice"] = i.hp_dice
            prepared_data.append(dicti)
            dicti = dict()            
        return prepared_data

    def __str__(self):
        return self.class_name

class Class_skills(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    @classmethod
    def parseClass_skills(self):
        data = list(self.objects.all())
        prepared_data  = list()
        dicti = dict()
        for i in data:
            dicti["id"] = i.id
            dicti["name"] = i.name
            dicti["class_id"] = i.class_id
            dicti["description"] = i.description
            prepared_data.append(dicti)
            dicti = dict()            
        return prepared_data

    def __str__(self):
        return self.name

#class Archetype_skills(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=100)
#    archetype_id = models.ForeignKey(Archetypes, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name

class Current_class_info(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Class_skills, on_delete=models.CASCADE)
    #archetype_id = models.ForeignKey(Archetype_skills, on_delete=models.CASCADE)

    @classmethod
    def parseCurrent_class_info(self):
        data = list(self.objects.all())
        prepared_data  = list()
        dicti = dict()
        for i in data:
            dicti["id"] = i.id
            dicti["class_id"] = i.class_id
            prepared_data.append(dicti)
            dicti = dict()            
        return prepared_data

class Player(models.Model):
    list_id = models.AutoField(primary_key=True)
    character_name = models.CharField(max_length=40)
    level = models.IntegerField()
    class_table = models.ForeignKey(Current_class_info, on_delete=models.CASCADE)
    race_id = models.ForeignKey(Races, on_delete=models.CASCADE)
    background_id = models.ForeignKey(Background, on_delete=models.CASCADE)
    alignment = models.CharField(max_length=2)
    hit_points = models.JSONField(default=list())
    experience = models.JSONField(default=list())
    stats = models.JSONField(default=dict())
    skills = models.JSONField(default=dict())
    gear = models.JSONField(default=dict())

    @classmethod
    def parsePlayer(self):
        data = list(self.objects.all())
        prepared_data  = list()
        dicti = dict()
        for i in data:
            dicti["list_id"] = i.list_id
            dicti["character_name"] = i.character_name
            dicti["level"] = i.level
            dicti["class_table"] = i.class_table
            dicti["race_id"] = i.race_id
            dicti["background_id"] = i.background_id
            dicti["alignment"] = i.alignment
            dicti["hit_points"] = i.hit_points
            dicti["experience"] = i.experience
            dicti["stats"] = i.stats
            dicti["skills"] = i.skills
            dicti["gear"] = i.gear
            prepared_data.append(dicti)
            dicti = dict()            
        return prepared_data

    def __str__(self):
        return self.character_name
