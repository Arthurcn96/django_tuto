from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getData),
    path('add/poll/', views.addPoll),
    path('add/question/', views.addQuestion),
    path('add/choice/', views.addChoice),
]
