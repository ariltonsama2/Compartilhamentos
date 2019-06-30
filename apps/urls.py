from django.urls import include, path
from django.contrib import admin

from theme import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', include('Games_fbv.urls', namespace='Games_fbv')),
]
