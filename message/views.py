from email import message
import imp
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
import requests
from django.conf import settings
from user.models import User
from message.models import *
from django.forms.models import model_to_dict
import time
import datetime
# Create your views here.

def getAllCompletedMessage(request):
    message_list=CompletedMessage.objects.all()

    # print(message_list)
    res=[]

    for i in range(len(message_list)):
        res.append(model_to_dict(message_list[i].message))
        res[i]['publisher'] = message_list[i].publisher.id
        res[i]['createdtime'] = str(message_list[i].message.createdtime)
        res[i]['createdtime'] = res[i]['createdtime'][0:10]
        imgList = list(MessageImg.objects.filter(message = message_list[i].message))
        res[i]['imgList'] = []
        for j in imgList:
            res[i]['imgList'].append('http://127.0.0.1:8080/media/img/'+str(j.imgSrc))
            
    for i in res:
        i['nickName'] = User.objects.get(id=i['publisher']).nickName
        i['userImg'] = User.objects.get(id=i['publisher']).userImg
        search_dict = dict()
        search_dict['user'] = i['publisher']
        search_dict['message'] = i['id']
        
        if (len(ReadMessage.objects.filter(**search_dict))>0):
            i['Read'] = True
        else:
            i['Read'] = False

        if (len(CollectMessage.objects.filter(**search_dict))>0):
            i['Collect'] = True
        else:
            i['Collect'] = False

        if len(i['content'])>12:
            i['shortContent'] = i['content'][0:10]+'...'
        else:
            i['shortContent'] = i['content']
        print(i['createdtime'])
    res.reverse()
    return JsonResponse({'ret':0,'message_list':res})

def collectMessage(request):
    data=request.params['data']
    print(data)
    search_dict = dict()
    search_dict['user'] = data['userId']
    search_dict['message'] = data['messageId']
    collect = CollectMessage.objects.filter(**search_dict)
    print(len(collect))
    for i in collect:
        print(i)
    if (len(collect)>0):
        print(1)
        for i in collect:
            i.delete()
    else:
        print(2)
        collectMessage =CollectMessage()
        collectMessage.user = User.objects.get(id=data['userId'])
        collectMessage.message = Message.objects.get(id=data['messageId'])
        # print(readMessage.user)
        # readMessage.message1 = User.objects.get(id=data['userId'])
        print(collectMessage.user)
        collectMessage.save()
    return JsonResponse({'ret':0})

def readMessage(request):
    data=request.params['data']
    print(data)
    readMessage = ReadMessage()
    readMessage.user = User.objects.get(id=data['userId'])
    readMessage.message = Message.objects.get(id=data['messageId'])
    readMessage.save() 
    return JsonResponse({'ret':0})

def addCompletedMessage(request):
    data = request.params['data']
    message = Message()
    completedMessage = CompletedMessage()
    message.title = data['title']
    message.content = data['content']
    message.classify = data['classify']
    message.classifyj = data['classifyj']
    try:
        completedMessage.publisher = User.objects.get(id=data['publisherId'])
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        message.save()
        completedMessage.message=message
        completedMessage.save()
        return JsonResponse({'ret':0,'messageId':message.id})

def addStagingAreaMessage(request):
    data = request.params['data']
    message = Message()
    stagingAreaMessage = StagingAreaMessage()
    message.title = data['title']
    message.content = data['content']
    message.classify = data['classify']
    message.classifyj = data['classifyj']
    try:
        stagingAreaMessage.publisher = User.objects.get(id=data['publisherId'])
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        message.save()
        stagingAreaMessage.message=message
        stagingAreaMessage.save()
        return JsonResponse({'ret':0,'messageId':message.id})

def addWastepaperBaskectMessage(request):
    data = request.params['data']
    message = Message()
    wastepaperBaskectMessage = WastepaperBaskectMessage()
    message.title = data['title']
    message.content = data['content']
    message.classify = data['classify']
    message.classifyj = data['classifyj']
    try:
        wastepaperBaskectMessage.publisher = User.objects.get(id=data['publisherId'])
    except BaseException:
        return JsonResponse({'ret': 1})
    else:
        message.save()
        wastepaperBaskectMessage.message=message
        wastepaperBaskectMessage.save()
        return JsonResponse({'ret':0,'messageId':message.id})

def addMessageImg(request):
    data = request.params['data']
    messageImg = MessageImg()
    messageImg.imgSrc = data['imgSrc']
    messageImg.message = Message.objects.get(id = data['messageId'])
    messageImg.save()
    return JsonResponse({'ret':0})

def getStagingAreaMessage(request):
    data = request.params['data']
    publisher = User.objects.get(id=data['publisherId'])
    message_list = StagingAreaMessage.objects.filter(publisher = publisher)
    res=[]
    for i in range(len(message_list)):
        res.append(model_to_dict(message_list[i].message))
        res[i]['publisher'] = message_list[i].publisher.id
        res[i]['createdtime'] = str(message_list[i].message.createdtime)
        res[i]['createdtime'] = res[i]['createdtime'][0:10]
        imgList = list(MessageImg.objects.filter(message = message_list[i].message))
        res[i]['imgList'] = []
        for j in imgList:
            res[i]['imgList'].append('http://127.0.0.1:8080/media/img/'+str(j.imgSrc))
            
    for i in res:
        i['nickName'] = User.objects.get(id=i['publisher']).nickName
        i['userImg'] = User.objects.get(id=i['publisher']).userImg
        search_dict = dict()
        search_dict['user'] = i['publisher']
        search_dict['message'] = i['id']
        
        if (len(ReadMessage.objects.filter(**search_dict))>0):
            i['Read'] = True
        else:
            i['Read'] = False

        if (len(CollectMessage.objects.filter(**search_dict))>0):
            i['Collect'] = True
        else:
            i['Collect'] = False

        if len(i['content'])>12:
            i['shortContent'] = i['content'][0:10]+'...'
        else:
            i['shortContent'] = i['content']
        print(i['createdtime'])
    res.reverse()
    return JsonResponse({'ret':0,'message_list':res})
    
def getWastepaperBaskectMessage(request):
    data = request.params['data']
    publisher = User.objects.get(id=data['publisherId'])
    message_list = WastepaperBaskectMessage.objects.filter(publisher = publisher)
    res=[]
    for i in range(len(message_list)):
        res.append(model_to_dict(message_list[i].message))
        res[i]['publisher'] = message_list[i].publisher.id
        res[i]['createdtime'] = str(message_list[i].message.createdtime)
        res[i]['createdtime'] = res[i]['createdtime'][0:10]
        imgList = list(MessageImg.objects.filter(message = message_list[i].message))
        res[i]['imgList'] = []
        for j in imgList:
            res[i]['imgList'].append('http://127.0.0.1:8080/media/img/'+str(j.imgSrc))
            
    for i in res:
        i['nickName'] = User.objects.get(id=i['publisher']).nickName
        i['userImg'] = User.objects.get(id=i['publisher']).userImg
        search_dict = dict()
        search_dict['user'] = i['publisher']
        search_dict['message'] = i['id']
        
        if (len(ReadMessage.objects.filter(**search_dict))>0):
            i['Read'] = True
        else:
            i['Read'] = False

        if (len(CollectMessage.objects.filter(**search_dict))>0):
            i['Collect'] = True
        else:
            i['Collect'] = False

        if len(i['content'])>12:
            i['shortContent'] = i['content'][0:10]+'...'
        else:
            i['shortContent'] = i['content']
        print(i['createdtime'])
    res.reverse()
    return JsonResponse({'ret':0,'message_list':res})

def deleteMessageFromStagingArea(request):
    data = request.params['data']
    message = Message.objects.get(id = data['messageId']) 
    stagingAreaMessage = StagingAreaMessage.objects.get(message = message)
    wastepaperBaskectMessage = WastepaperBaskectMessage()
    wastepaperBaskectMessage.message=message
    wastepaperBaskectMessage.publisher = stagingAreaMessage.publisher
    wastepaperBaskectMessage.save()
    stagingAreaMessage.delete()
    return JsonResponse({'ret':0})

def deleteMessageFromWastepaperBaskect(request):
    data = request.params['data']
    message = Message.objects.get(id = data['messageId']) 
    wastepaperBaskectMessage = WastepaperBaskectMessage.objects.get(message = message)
    wastepaperBaskectMessage.delete()
    return JsonResponse({'ret':0})

def dispatcher(request):
    if request.method == 'GET':
        request.params = request.GET
        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    action = request.params['action']


    if action == 'getAllCompletedMessage':
        return getAllCompletedMessage(request)
    elif action == 'collectMessage':
        return collectMessage(request)
    elif action == 'readMessage':
        return readMessage(request)
    elif action == 'addCompletedMessage':
        return addCompletedMessage(request)
    elif action == 'addStagingAreaMessage':
        return addStagingAreaMessage(request)
    elif action == 'addWastepaperBaskectMessage':
        return addWastepaperBaskectMessage(request)
    elif action == 'addMessageImg':
        return addMessageImg(request)
    elif action == 'getStagingAreaMessage':
        return getStagingAreaMessage(request)
    elif action == 'getWastepaperBaskectMessage':
        return getWastepaperBaskectMessage(request)
    elif action == 'deleteMessageFromStagingArea':
        return deleteMessageFromStagingArea(request)
    elif action == 'deleteMessageFromWastepaperBaskect':
        return deleteMessageFromWastepaperBaskect(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
        