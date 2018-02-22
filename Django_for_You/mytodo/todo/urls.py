from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addToDo,name='add'),
    path('complete/<todo_id>',views.complete_todo,name='complete'),
    path('deletecomplte',views.delete_completed,name='deletecomplete'),
    path('deleteall',views.delete_all,name='deleteall')
]