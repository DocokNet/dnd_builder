# Generated by Django 5.1.2 on 2024-12-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndpage', '0003_alter_class_skills_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_skills',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
