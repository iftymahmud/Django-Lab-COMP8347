# carapp/urls.py

from django.urls import path
from . import views
from .views import AboutUsView

app_name = 'carapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),
    path('team/', views.team_members, name='team_members'),
]