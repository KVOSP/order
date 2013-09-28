# -*- coding: utf-8 -*- 
from django.http import HttpResponse
    
def WebHome(request):
	if ('city' in request.session):
		citys = request.session['city']
	else:
		citys = '�Ͼ�'
    line = {}
    matrix = []
    """
    foodName = []
    restName = []
    address = []
    """
    rID = db_restaurant.get(city = citys).restID
    m = db_food.objects.filter(city = citys, spec = 'true').order_by("restID_id")
            for i in m:
                #�������������ַ�ʽ����ʵ��,����ֻ��������
                line['foodName']=db_food.objects.get(foodID = i.foodID).foodName
                line['restName'] = db_restaurant.objects.get(restID = i.restID).restName
                line['address'] = db_restaurant.objects.get(restID = i.restID).address
                matrix.append(dict(line))
    t = get_template('WebHome.html')       
    html = t.render(Context({'matrix':matrix, 'title':"�Ƽ��˵�",}))    
    return HttpResponse(html)
    
def rest(request, offset):
	line = {}
    matrix = []
    """
    foodName = []
    restName = []
    spec = []
    """
    m = db_food.objects.filter(restID_id = offset).order_by("spec")
            for i in m:
                #�������������ַ�ʽ����ʵ��,����ֻ��������
                line['foodName']=db_food.objects.get(foodID = i.foodID).foodName
                line['restName'] = db_restaurant.objects.get(restID = i.restID_id).restName
                line['spec'] = db_food.objects.get(foodID = i.foodID).spec
                matrix.append(dict(line))
    t = get_template('rest.html')       
    html = t.render(Context({'matrix':matrix, 'title':"����˵�",}))    
    return HttpResponse(html)