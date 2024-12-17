from django.db import models

class Player(models.Model):
    list_id = models.AutoField(primary_key=True)
    character_name = models.CharField(max_length=40)
    level = models.IntegerField()
    class_table = models.ForeignKey(Current_class_info, on_delete=models.CASCADE)
    race_id = models.ForeignKey(Races, on_delete=models.CASCADE)
    background_id = models.ForeignKey(Background, on_delete=models.CASCADE)
    alignment = models.CharField(max_length=2)

class Current_class_info(models.Model):
    id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Class_skills, on_delete=models.CASCADE)