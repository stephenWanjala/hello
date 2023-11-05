from django.urls import path

from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_todo, name='create_todo'),
    path('detail/<int:pk>/', views.todo_detail, name='todo_detail'),
]