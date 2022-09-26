import imp
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
import requests
from django.conf import settings
from .models import User
from django.forms.models import model_to_dict
# Create your views here.

def login(request):
    data=request.params['data']
    user = User()
    try:
        user1 = User.objects.get(userName=data['userName'])
    except User.DoesNotExist:
        return JsonResponse({'ret':0,'msg':'error'})
    if user1.password == data['password']:
        return JsonResponse({'ret':0,'msg':'success','userData':model_to_dict(user1)})
    else:
        return JsonResponse({'ret':0,'msg':'error'})

def changeUserImg(request):
    data=request.params['data']
    print(data)
    user = User()
    try:
        user1 = User.objects.get(id=data['id'])
    except User.DoesNotExist:
        return JsonResponse({'ret':0,'msg':'error'})
    else:
        user1.userImg='http://127.0.0.1:8080/media/img/'+data['filePath']
        user1.save()
        return JsonResponse({'ret':0,'msg':'success','filePath':user1.userImg})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    action = request.params['action']


    if action == 'login':
        return login(request)
    elif action == 'changeUserImg':
        return changeUserImg(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})