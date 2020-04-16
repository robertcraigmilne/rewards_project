from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # This is the default path to default ADMIN screen
    path('pointsApp/', include('pointsApp.urls')) # This links other APPS within Project 'rewards' - there starting point
        # <ip:8000>/pointsAppDir will call /rewards_project/pointsAppDir/*  where * replace '' means home or '/list'
   ]
