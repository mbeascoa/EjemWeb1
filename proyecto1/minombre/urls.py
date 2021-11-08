from django.urls import path

from minombre import views

urlpatterns=[
    path('',views.index,name='index')
]