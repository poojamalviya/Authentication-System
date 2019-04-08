# -*- coding: utf-8 -*-
# Create your models here.
from __future__ import unicode_literals
# from django.db import models
from djongo import  models
import datetime


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255, default="pooja", editable=False)
    email = models.CharField(max_length=255, default="poojamalviya7760@gmail.com", editable=False)
    password = models.CharField(max_length=255, default="pooja@123", editable=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.name

    # def to_json(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'desc': self.description,
    #         'price': self.price,
    #         'date_created': self.date_created,
    #         'date_modified': self.date_modified
    #     }