from django.contrib import admin
from django.urls import path, include
from ToDo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),

    path('todo/', include('ToDo.urls')),
]
