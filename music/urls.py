from django.urls import path
from . import views


app_name = 'music'


urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    
    # /music/712
    path('<album_id>/', views.detail, name='detail'),

    # /music/712/favourite/
    path('<album_id>/favourite/', views.favourite, name='favourite'),
]
