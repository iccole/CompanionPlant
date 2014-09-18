from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import RequestContext, loader
from django.db.models import Q

# Create your views here.
import csv
from plants.models import Plant, PlantMatch

def index(request):
	plants = Plant.objects.all()
	context = {'plants': plants}
	return render(request, 'plants/index.html', context)

def plant(request, plant_id):
	plants = Plant.objects.all()
	plant = get_object_or_404(Plant, id=plant_id)
	helps = PlantMatch.objects.all().filter(plant1=plant_id, relationship="HLP")
	helpedBy = PlantMatch.objects.all().filter(plant2 = plant_id, relationship="HLP")
	avoid = PlantMatch.objects.all().filter(Q(plant1 = plant_id) | Q(plant2 = plant_id), relationship="HRT") 
	context = {'plant' : plant, 'helps' : helps, 'helpedBy' : helpedBy, 'avoid' : avoid, 'plants': plants}
	return render(request, 'plants/plantView.html', context)

def addMatch(request):
	plant_1 = request.POST['plant1']
	plant_2 = request.POST['plant2']
	relationship = request.POST['relationship']
	match = PlantMatch.objects.get_or_create(plant1_id= plant_1, plant2_id= plant_2, relationship=relationship)
	# if relationship is "HLP":
	# 	match = PlantMatch.objects.get_or_create(plant1_id= plant_1, plant2_id= plant_2, relationship=relationship)
	# else if relationship is "HRT":
	# 	match = PlantMatch.objects.get_or_create(plant1_id= plant_1, plant2_id= plant_2, relationship=relationship)
	# else if relationship is "RPL":
	# 	match = PlantMatch.objects.get_or_create(plant1_id= plant_1, plant2_id= plant_2, relationship=relationship)
	# else if relationship is "ATR":
	# 	match = PlantMatch.objects.get_or_create(plant1_id= plant_1, plant2_id= plant_2, relationship=relationship)
	return HttpResponse("success")
def createMatch(request):
	plant_options = Plant.objects.all()
	context = {'plants' : plant_options}
	return render(request, 'plants/addMatch.html', context)