
from django.contrib import admin
from django.urls import path
from app.views import home , login , signup , add_todo , signout , delete_todo, change_todo,mark_as_complete,mark_as_incomplete,edit_todo,completion


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
    path('mark_complete/<int:id>/',mark_as_complete, name='mark_as_complete'),
    path('mark_incomplete/<int:id>/',mark_as_incomplete, name='mark_as_incomplete'),
    path('edit_todo/<int:id>/',edit_todo, name='edit_todo'),
    path('complete/', completion, name = 'complete'),
]