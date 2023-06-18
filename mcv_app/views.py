from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,DetailView
from django.contrib.auth import authenticate , login ,logout
from .models import *
from .forms import *
from django.contrib import messages
import requests
class SplashPageView(TemplateView):
    template_name = 'spalsh_page.html'    


class MCVAdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and MCVUser.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/home/')
        return super().dispatch(request, *args, **kwargs)

class MCVDriverRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Driver.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/driver-car-detail/')
        return super().dispatch(request, *args, **kwargs)

class HomePageView(MCVAdminRequiredMixin,TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car-detail"] =  Car.objects.latest('id')
        context["all_cars"] = Car.objects.all().order_by("-id")
        return context
    

class DashBoardPageView(MCVAdminRequiredMixin,DetailView):
    template_name = 'dashboard.html'
    model = Car
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_admin_user = MCVUser.objects.get(user=self.request.user)
        context["all_cars"] = Car.objects.all().order_by("-id")
        context["car_detail"] = Car.objects.get(id=self.kwargs['pk'])
        context["driver"] = Driver.objects.get(drive_car=context["car_detail"].id) if context["car_detail"] != None else None
        context["last_cars"] = Car.objects.all().exclude(id=self.kwargs['pk'])
        context["lon_src"] = float(current_admin_user.Longitude)  
        context["lat_src"] = float(current_admin_user.Latitude )
        context["lon_des"] = float(context["car_detail"].Longitude) 
        context["lat_des"] = float(context["car_detail"].Latitude) 
        return context

class McvUserLogin(FormView):
    template_name = "mcv_user_login.html"
    form_class = McvUserLoginForm
    success_url = '/home/'
    
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and MCVUser.objects.filter(user=usr).exists():
            login(self.request, usr)
            return super().form_valid(form)
        else:
            messages.error(self.request,'The admin username or password not correct please try again !')
            return redirect('/admin-login/')
    
class McvDriverLogin(FormView):
    template_name= "mcv_driver_login.html"
    form_class = McvDriverLoginForm
    success_url = '/driver-car-detail/'
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None and Driver.objects.filter(user=user).exists():
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request,'The driver username or password not correct please try again !')
            return redirect('/driver-login/')

class DriverDashBoardPageView(MCVDriverRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_driver = self.request.user
        context["driver"] = Driver.objects.get(user=current_driver)
        context["car_detail"] = context["driver"].drive_car
        context["lon_des"] = float(context["car_detail"].Longitude) 
        context["lat_des"] = float(context["car_detail"].Latitude)
        return context