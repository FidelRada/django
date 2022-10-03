from django.urls import path
from . import views

urlpatterns  = [
    path('', views.hello),
    path('hello/', views.hello),
    path('about/<str:username>', views.about),
    path('project/', views.projects),
    path('task/<int:id>', views.tasks)
]