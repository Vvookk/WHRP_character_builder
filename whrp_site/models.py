from django.db import models

# Create your models here.

class RaceModel(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    abilities = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    

class CharacteristicsModel(models.Model):
    name = models.CharField(max_length=20)
    short = models.CharField(max_length=5)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
class CareerModel(models.Model):
    name = models.CharField(max_length=30)
    stats = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    abilities = models.TextField(max_length=1000)
    equipment = models.TextField(max_length=1000)
    career_entries = models.TextField(max_length=1000)
    career_exits = models.TextField(max_length=1000)
    is_basic = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SkillsModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    characteristic = models.ForeignKey(CharacteristicsModel)

    def __str__(self):
        return self.name
    
class AbilitiesModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    characteristic = models.ForeignKey(CharacteristicsModel)

    def __str__(self):
        return self.name