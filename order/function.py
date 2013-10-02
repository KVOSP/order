# -*- coding: utf-8 -*- 
from django.http import HttpResponse
from db.models import * 
from django.template import  Context
from django.template.loader import get_template
    
def WebHome(request):
	if 'city' in request.session and request.session['city']:
		citys = request.session['city']
	else:
		citys = '南京'
	line = {}
	matrix = []
	"""
	foodName = []
	restName = []
	address = []
	"""
	try:
		rID = restaurant.objects.get(city = citys).restID
	except:
		pass
	m =   restaurant.objects.filter(city = citys).order_by("restID")
	for i in m:
				line['foodName']=food.objects.get(foodID = i.foodID).foodName
				line['restName'] = restaurant.objects.get(restID = i.restID).restName
				line['address'] = restaurant.objects.get(restID = i.restID).address
				matrix.append(dict(line))
	t = get_template('WebHome.html')       
	html = t.render(Context({'matrix':matrix, 'title':"1",}))    
	return HttpResponse(html)
    
def rest(request, offset):
	line = {}
	matrix = []
	"""
	foodName = []
	restName = []
	spec = []
	"""
	m = food.objects.filter(restID_id = offset).order_by("spec")
	for i in m:
		line['foodName']=food.objects.get(foodID = i.foodID).foodName
		line['restName'] = restaurant.objects.get(restID = i.restID_id).restName
		line['spec'] = food.objects.get(foodID = i.foodID).spec
		matrix.append(dict(line))
	t = get_template('rest.html')       
	html = t.render(Context({'matrix':matrix, 'title':"2",}))    
	return HttpResponse(html)