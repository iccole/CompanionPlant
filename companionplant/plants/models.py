from django.db import models

# Create your models here.

class Plant(models.Model):
	# def_init_(self, arg):
	# 	super(Plant, self).__init__()
	# 	self.arg = arg
	name = models.CharField(max_length=150)
	scientificName = models.CharField(max_length=300, null=True)
	description = models.CharField(max_length=3000, null=True)

class Pest(models.Model):
	# """docstring for Pest"""
	# def __init__(self, arg):
	# 	super(Pest, self).__init__()
	# 	self.arg = arg
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=3000)

class PlantMatch(models.Model):
	# """docstring for PlantMatch"""
	# def __init__(self, arg):
	# 	super(PlantMatch, self).__init__()
	# 	self.arg = arg
	plant1 = models.ForeignKey(Plant, related_name='first_plant')
	plant2 = models.ForeignKey(Plant, related_name='second_plant')
	relationship = models.CharField(max_length=3)
	
class PestMatch(models.Model):
	# """docstring for PestMatch"""
	# def __init__(self, arg):
	# 	super(PestMatch, self).__init__()
	# 	self.arg = arg
	plant = models.ForeignKey(Plant)
	pest = models.ForeignKey(Pest)

		