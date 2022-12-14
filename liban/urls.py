"""liban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/liban/user/', include('user.urls')),
    path('api/liban/addpic/',include('addpic.urls')),
    path('api/liban/message/',include('message.urls'))
    # path('Catpus/user/',include('user.urls')),
    # path('Catpus/cat/',include('cat.urls')),
    # path('Catpus/likes/',include('likes.urls')),
    # path('Catpus/moments/',include('moments.urls')),
    # path('Catpus/tweet/',include('tweet.urls')),
    # path('Catpus/addpic',views.addpic)
    # path('img/', include('showpic.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)