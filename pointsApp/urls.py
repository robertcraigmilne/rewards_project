from django.urls import path, include  # PATH and INCLUDE are class based views
from pointsApp import views  #views.py has function based views

# all the paths below are accessed by http:<ip>:8000/pointsAppDir/ this is home page with members_form
# which handles insert, update, delete functions
# and the 2nd page http:<ip>:8000/pointsAppDir/list/ this is a page to LIST the members in the database

#path(<positional arg>, <function to call>, <argument e.g. name=<name of URL> so can reference from HTML>)

urlpatterns = [
    path('', views.members_form, name='member_insert'), # really its 'pointsApp/insert/' and call function 'member_insert'
    path('Members/', views.members_list, name='member_list'), #pointsApp/list
    path('list/', views.members_list, name='member_list'), #pointsApp/list
    path('update/<int:id>/', views.members_form, name='member_update'), #pointsApp/update/5 or whatever db row PK is  
    path('delete/<int:id>/', views.members_delete, name='member_delete'),#pointsApp/delete/5 or whatever db row PK is
    path('Resorts/', views.resorts_list, name='resort_list'), # CRUD for Resorts table
    path('resortinsert/', views.resorts_form, name='resort_insert'), 
    path('resortlist/', views.resorts_list, name='resort_list'), 
    path('resortupdate/<int:id>/', views.resorts_form, name='resort_update'),   
    path('resortdelete/<int:id>/', views.resorts_delete, name='resort_delete'),
    path('Points/', views.points_list, name='point_list'), # CRUD for Points table
    path('pointinsert/', views.points_form, name='point_insert'), 
    path('pointlist/', views.points_list, name='point_list'), 
    path('pointupdate/<int:id>/', views.points_form, name='point_update'),   
    path('pointdelete/<int:id>/', views.points_delete, name='point_delete'),
   ]
