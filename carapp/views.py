# carapp/views.py

from django.http import HttpResponse
from .models import CarType, Vehicle, TeamMember, OrderVehicle, Buyer
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from .models import Buyer


def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')

    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1

    context = {
        'cartype_list': cartype_list,
        'visit_count': visit_count + 1,
    }

    response = render(request, 'carapp/homepage.html', context)
    # Set a cookie named 'cookie_counter' that expires in 10 seconds
    response.set_cookie('cookie_counter', 'Cookie Value', max_age=10)
    return response




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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('carapp:login')
    template_name = 'carapp/signup.html'

    def form_valid(self, form):
        # Save the User instance directly
        response = super().form_valid(form)

        # At this point, 'form.instance' is already the saved User object
        # If you need additional fields, set them here
        # For example:
        user = form.instance
        user.save()

        return response


def login_here(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        print(f"Username: {username}, Password: {password}")  # Debug

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('carapp:homepage'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Login details are incorrect.')
    else:
        return render(request, 'carapp/login_here.html')

@login_required
def logout_here(request):
    logout(request)
    return HttpResponseRedirect(reverse('carapp:homepage'))

@login_required
def list_of_orders(request):
    user = request.user
    try:
        buyer = Buyer.objects.get(id=user.id)
        orders = OrderVehicle.objects.filter(buyer=buyer)
        if orders.exists():
            return render(request, 'carapp/list_of_orders.html', {'orders': orders})
        else:
            message = 'You have not placed any orders.'
            return render(request, 'carapp/list_of_orders.html', {'message': message})
    except Buyer.DoesNotExist:
        return HttpResponse('You are not registered.')
