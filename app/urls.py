
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('' , views.home , name='home' ), 
   path('login/' ,views.login  , name='login'), 
   path('signup/' , views.signup ), 
   path('profile/' , views.profile, name="profile" ), 
   path('add-todo/' , views.add_todo ), 
   path('delete-todo/<int:id>' , views.delete_todo ), 
   path('change-status/<int:id>/<str:status>' , views.change_todo ), 
   path('logout/' , views.signout ), 
    path('mark_complete/<int:id>/',views.mark_as_complete, name='mark_as_complete'),
    path('mark_incomplete/<int:id>/',views.mark_as_incomplete, name='mark_as_incomplete'),
    path('edit_todo/<int:id>/',views.edit_todo, name='edit_todo'),
    path('complete/', views.completion, name = 'complete'),
]