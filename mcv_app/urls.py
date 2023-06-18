from django.urls import path
from .views import *
from . import api

app_name = 'mcv_app'

urlpatterns = [
    path("", SplashPageView.as_view(), name="splash"),
    path("admin-login/", McvUserLogin.as_view(), name="mcv_admin_login"),
    path("driver-login/", McvDriverLogin.as_view(), name="mcv_driver_login"),
    path('home/',HomePageView.as_view(),name='home'),
    path("dashboard/<int:pk>/", DashBoardPageView.as_view(), name="dashboard"),
    path("driver-car-detail/", DriverDashBoardPageView.as_view(), name="driver_dashboard"),
      # cars Api url
    path("api/car-list/", api.CarListApi.as_view(), name="api_car_list"),
    path("api/car-detail/<int:pk>", api.CarDetailApi.as_view(), name="api_car_detail"),
    path("api/car-filter/<str:kw>", api.CarFilterApi.as_view(), name="api_car_filter"),
    # cardiagnostic Api url
    path("api/cardiagnostic-list/",api.CarDiagnosticListApi.as_view(),name="api_cardiagnostic_list"),
    path("api/cardiagnostic-detail/<int:pk>",api.CarDiagnosticDetailApi.as_view(),name="api_cardiagnostic_detail"),
    path("api/cardiagnostic-filter/<str:kw>",api.CarDiagnosticFilterApi.as_view(),name="api_cardiagnostic_filter"),
    # drivers Api url
    path("api/driver-list/", api.DriverListApi.as_view(), name="api_Drivers_list"),
    path("api/driver-detail/<int:pk>",api.DriverDetailApi.as_view(),name="api_Drivers_list"),
    path("api/driver-filter/<str:kw>",api.DriverFilterApi.as_view(),name="api_Drivers_filter"),
    # admin Api url
    path("api/admin-list/", api.AdminListApi.as_view(), name="api_admins_list"),
    path("api/admin-detail/<int:pk>",api.AdminDetailApi.as_view(),name="api_admins_list"),
    path("api/admin-filter/<str:kw>",api.AdminFilterApi.as_view(),name="api_admins_filter"),
    
    path('api/my-car/<int:pk>/', api.CarDriverUpdateView.as_view(), name='car-driver-update'),
]
