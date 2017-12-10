from django.urls import path
from . import views


urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    
    # /music/712
    path('<album_id>/', views.detail, name='detail'),
]
