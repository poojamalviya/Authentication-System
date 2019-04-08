# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
# from models import Product
from django.http import HttpResponse
from django.core.cache import cache
import json
from mongoengine import *
from mongoengine import connect
import uuid



from .models import User

connect('my_db')


def index(request):
    return render_to_response('index.html')

def login(request):
    return render_to_response('login.html')


# {
# 	"_id" : ObjectId("5cab2168db016a929915d89e"),
# 	"id" : 3,
# 	"name" : "pooja",
# 	"email" : "poojamalviya7760@gmail.com",
# 	"password" : "pooja@123",
# 	"date_created" : ISODate("2019-04-08T10:24:40.748Z"),
# 	"date_modified" : ISODate("2019-04-08T10:24:40.748Z")
# }

def authenticate(request):

    name = request.POST.get("name")

    user_data= User.objects.get(name= name)

    if user_data is None:

        return HttpResponse(json.dumps({"status": 410, "message": "User Not Found"}), mimetype = 'application/json')

    if user_data != request.password:

        return HttpResponse(json.dumps({"status": 410, "message":"Incorrect Password"}), mimetype='application/json')

    else:

        bearerToken = name + ':' +uuid.uuid1()

        cache.set(name, bearerToken , timeout=30)

        return HttpResponse(json.dumps({"status": 200, "Token":bearerToken}), mimetype='application/json')




def validate(request):

    tokenString = request.GET.get("token")
    getName = tokenString.split(':')

    name = getName[0]

    checkInCache = cache.get(name)

    if checkInCache is not None:
        return HttpResponse(json.dumps({"status": 200, "message": True}),
                            mimetype='application/json')
    else:
        return HttpResponse(json.dumps({"status": 410, "message": False}),
                            mimetype='application/json')



