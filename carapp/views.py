# carapp/views.py

from django.http import HttpResponse
from .models import CarType, Vehicle, TeamMember
from django.shortcuts import get_object_or_404
from django.views import View


def homepage(request):
    vehicle_list = Vehicle.objects.all().order_by('car_price')[:15]
    response = HttpResponse()
    heading1 = '<p>Top 15 Vehicles by Price (Ascending):</p>'
    response.write(heading1)
    for vehicle in vehicle_list:
        para = f'<p>{vehicle.id}: {vehicle.car_name} - ${vehicle.car_price}</p>'
        response.write(para)
    return response


# This AboutUs is converted to CBV
class AboutUsView(View):
    def get(self, request):
        vehicles = Vehicle.objects.all().order_by('car_price')
        response = HttpResponse()
        response.write('<h1>About Us</h1>')
        response.write('<p>This is a Car Showroom.</p>')
        response.write('<h2>Our Vehicles:</h2>')
        for vehicle in vehicles:
            response.write(f'<p>{vehicle.car_name}: ${vehicle.car_price}</p>')
        return response

def cardetail(request, cartype_no):
    cartype = get_object_or_404(CarType, pk=cartype_no)
    vehicles = Vehicle.objects.filter(car_type=cartype)
    response = HttpResponse()
    heading1 = f'<p>Vehicles for Car Type: {cartype.name}</p>'
    response.write(heading1)
    for vehicle in vehicles:
        para = f'<p>{vehicle.id}: {vehicle.car_name} - ${vehicle.car_price}</p>'
        response.write(para)
    return response

def team_members(request):
    members = TeamMember.objects.all()
    response = HttpResponse()
    heading1 = '<p>Team Members:</p>'
    response.write(heading1)
    for member in members:
        para = f"<p>{member.last_name} {member.first_name}, Semester {member.semester}, Link: <a href='{member.personal_link}'>{member.personal_link}</a></p>"
        response.write(para)
    return response

