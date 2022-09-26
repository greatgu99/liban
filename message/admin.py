from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','title','createdtime']

@admin.register(CompletedMessage)
class CompletedMessageAdmin(admin.ModelAdmin):
    list_display = ['id','message','publisher']


@admin.register(StagingAreaMessage)
class StagingAreaMessageAdmin(admin.ModelAdmin):
    list_display = ['id','message','publisher']

@admin.register(WastepaperBaskectMessage)
class WastepaperBaskectMessageAdmin(admin.ModelAdmin):
    list_display = ['id','message','publisher']

@admin.register(ReadMessage)
class ReadMessageAdmin(admin.ModelAdmin):
    list_display = ['id','user','message']

@admin.register(CollectMessage)
class CollectMessageAdmin(admin.ModelAdmin):
    list_display = ['id','user','message']

    
@admin.register(MessageImg)
class MessageImgAdmin(admin.ModelAdmin):
    list_display = ['id','message','imgSrc','createdtime']