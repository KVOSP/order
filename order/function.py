# -*- coding: utf-8 -*- 
from django.http import HttpResponse
    
def WebHome(request):
	if ('city' in request.session):
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
    m = db_food.objects.filter(city = citys, spec = 'true').order_by("restID_id")
            for i in m:
                #迭代、序列两种方式可以实现,这里只能用序列
                line['foodName']=db_food.objects.get(foodID = i.foodID).foodName
                line['restName'] = db_restaurant.objects.get(restID = i.restID).restName
                line['address'] = db_restaurant.objects.get(restID = i.restID).address
                matrix.append(dict(line))
    t = get_template('WebHome.html')       
    html = t.render(Context({'matrix':matrix, 'title':"推荐菜单",}))    
    return HttpResponse(html)
    
def rest(request, offset):
    return HttpResponse("Hello world")