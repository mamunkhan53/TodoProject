from django.urls import path
from .views import *

urlpatterns = [
    path('addTask/', addTask, name="addTask"),
    path('mark_as_done/<int:pk>/', mark_as_done, name="mark_as_done"),
    path('mark_as_undone/<int:pk>/', mark_as_undone, name="mark_as_undone"),
    path('editTask/<int:pk>/', editTask, name="editTask"),
    path('delete/<int:pk>/', delete, name="delete"),    
]
