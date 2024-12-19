from django.db import models
from jsonfield import JSONField

class Races(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    pros = models.JSONField(default=dict())
    cons = models.JSONField(default=dict())
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Background(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    background_skills = models.JSONField(default=list())
    languages = models.JSONField(default=list())
    instruments_prof = models.JSONField(default=list())
    background_gear = models.JSONField(default=list())

    def __str__(self):
        return self.name

class Archetypes(models.Model):
    id = models.AutoField(primary_key=True)
    archetype_name = models.CharField(max_length=30)

    def __str__(self):
        return self.archetype_name

class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=20)
    hp_dice = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name

class Class_skills(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Archetype_skills(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    archetype_id = models.ForeignKey(Archetypes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Current_class_info(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Class_skills, on_delete=models.CASCADE)
    archetype_id = models.ForeignKey(Archetype_skills, on_delete=models.CASCADE)


class Player(models.Model):
    list_id = models.AutoField(primary_key=True)
    character_name = models.CharField(max_length=40)
    level = models.IntegerField()
    class_table = models.ForeignKey(Current_class_info, on_delete=models.CASCADE)
    race_id = models.ForeignKey(Races, on_delete=models.CASCADE)
    background_id = models.ForeignKey(Background, on_delete=models.CASCADE)
    alignment = models.CharField(max_length=2)
    experience = models.JSONField(default=list())
    stats = models.JSONField(default=dict())
    skills = models.JSONField(default=dict())
    gear = models.JSONField(default=dict())

    def __str__(self):
        return self.character_name
