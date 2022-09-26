from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
import requests
from django.conf import settings
import os
from pathlib import Path
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.forms.models import model_to_dict
from django.core import serializers

def addpic(request):
    print("!!!!!!!!!!!!!!!!!!!")
    img = request.FILES.get('file')
    
    # 此处img_sec_check有待改进 包含更多返回值
    # if not img_sec_check(img):
    #     return JsonResponse({'ret':87014,'msg':'图片含有违规内容'})

    if not img:
        return JsonResponse({'ret': 1, 'msg': '请上传图片'})
    else:
        print('--------')
        print(img.name)
        print(img.size)
        print('--------')
        BASE_DIR = Path(__file__).resolve().parent.parent
        img.seek(0)
        path=default_storage.save('img/'+img.name,ContentFile(img.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return JsonResponse({'ret':0,'filePath':img.name})
