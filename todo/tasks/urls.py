from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home ,name="index"),
    path('', views.home, name='root'),
    path('update_task/<str:primarykey>/', views.updateTask, name="update_task"),
    path('delete_task/<str:primarykey>/', views.deleteTask, name="delete_task"),
    
]