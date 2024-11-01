# carapp/views.py

from django.http import HttpResponse
from .models import CarType, Vehicle, TeamMember
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render


def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    # Passing 'cartype_list' as an extra context variable to the template
    return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list})



# This AboutUs is converted to CBV
class AboutUsView(View):
    def get(self, request):
        vehicles = Vehicle.objects.all().order_by('car_price')
        # Passing 'vehicles' as an extra context variable to the template
        return render(request, 'carapp/aboutus.html', {'vehicles': vehicles})



def cardetail(request, cartype_no):
    cartype = get_object_or_404(CarType, pk=cartype_no)
    vehicles = Vehicle.objects.filter(car_type=cartype)
    # Passing 'cartype' and 'vehicles' as extra context variables to the template
    context = {
        'cartype': cartype,
        'vehicles': vehicles
    }
    return render(request, 'carapp/cardetail.html', context)


class TeamMembersView(View):
    def get(self, request):
        members = TeamMember.objects.all()
        # Passing 'members' as an extra context variable to the template
        return render(request, 'carapp/team_members.html', {'members': members})


def vehicles(request):
    vehicles_list = Vehicle.objects.all()
    return render(request, 'carapp/vehicles.html', {'vehicles_list': vehicles_list})

def orderhere(request):
    return HttpResponse("You can place your order here.")
