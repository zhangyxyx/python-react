from django.db import models
import django.utils.timezone as timezone
# -*- coding: utf-8 -*-
# Create your models here.
class Mobile(models.Model):
    brand = models.IntegerField()
    size = models.FloatField()
    price = models.IntegerField()
    # age = models.IntegerField()
    print(brand)
    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self
class User(models.Model):
    user = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    age = models.IntegerField()
    sign = models.CharField(max_length=45)
    job = models.CharField(max_length=45)
    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self


class Question(models.Model):
    title = models.CharField(max_length=45 , default="moren")
    econtent = models.TextField(default="moren")
    user = models.CharField(max_length=45,default="moren")
    time = models.CharField(max_length=45 , default="moren")
    etype = models.CharField(max_length=45 , default="moren")

    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self

class Essay(models.Model):
    title = models.CharField(max_length=45, default="moren")
    summary = models.CharField(max_length=45, default="moren")
    author = models.CharField(max_length=45, default="moren")
    time = models.CharField(max_length=45, default="moren")

    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self
