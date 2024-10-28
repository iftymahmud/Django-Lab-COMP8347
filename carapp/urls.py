# carapp/urls.py

from django.urls import path
from . import views
from .views import AboutUsView, TeamMembersView


app_name = 'carapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),
    path('team/', TeamMembersView.as_view(), name='team_members'),

]