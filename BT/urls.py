"""BT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from main_app import views as MA_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MA_views.home, name = 'home'),
    #Drills
    path('drills/',MA_views.drills,name ='drills'),
    path('drills/Fundamentals', MA_views.Fundamentals,name ='Fundamentals'),
    path('drills/Shotmaking', MA_views.Shotmaking,name ='Shotmaking'),
    path('drills/Kicking', MA_views.Kicking,name ='Kicking'),
    path('drills/Banking', MA_views.Banking,name ='Banking'),
    path('drills/Safety', MA_views.Safety,name ='Safety'),
    path('drills/Jumping', MA_views.Jumping,name ='Jumping'),
    path('drills/fundamentals/stop', MA_views.stop,name ='stop'),
    path('drills/fundamentals/follow', MA_views.follow,name ='follow'),
    path('drills/fundamentals/draw', MA_views.draw,name ='draw'),
    path('drills/shotmaking/mill', MA_views.mill,name ='mill'),
    path('drills/shotmaking/everest', MA_views.everest,name ='everest')
    
    
    
]
