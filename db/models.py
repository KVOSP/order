from django.db import models
#coding=utf-8
# Create your models here.

class restaurant(models.Model):
    def __unicode__(self):
            return self.title
    restID = models.IntegerField(primary_key=True)
    restName =  models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    search_fields = ('restID', 'restName')
    
class food(models.Model):
    def __unicode__(self):
            return self.title
    foodID = models.IntegerField(primary_key=True)
    foodName =  models.CharField(max_length=50)
    restID = models.ForeignKey('restaurant')
    spec = models.BooleanField()
    search_fields = ('foodID', 'foodName')
    