from django.urls import path

from Games_fbv import views

app_name = 'Games_fbv'


#Casamento de URLs
urlpatterns = [
 
  path('', views.Game_list, name='Game_list'),
  path('new', views.Game_create, name='Game_new'),
  path('edit/<int:pk>', views.Game_update, name='Game_edit'),
  path('delete/<int:pk>', views.Game_delete, name='Game_delete'),
]