from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),

  # path( 'oper/',views.operations,name='addition'),
  # path( 'oper/',views.operations,name='subtraction'),
  # path( 'oper/',views.operations,name='multiplication'),
   #path( 'oper/',views.operations,name='division'),

]