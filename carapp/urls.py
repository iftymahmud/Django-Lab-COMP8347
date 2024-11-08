# carapp/urls.py

from django.urls import path
from . import views
from .views import AboutUsView, TeamMembersView, SignUpView


app_name = 'carapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('<int:cartype_no>/', views.cardetail, name='cardetail'),
    path('team/', TeamMembersView.as_view(), name='team_members'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('order/', views.orderhere, name='orderhere'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.login_here, name='login'),
    path('logout/', views.logout_here, name='logout'),
    path('myorders/', views.list_of_orders, name='myorders'),
]