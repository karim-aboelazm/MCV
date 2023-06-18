from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Car(models.Model):
    car_id              = models.CharField(max_length=10) # a b c 1 2 3
    car_speed           = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    car_rpm             = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(9.0)])
    car_distance        = models.PositiveIntegerField(default=0)
    car_run_time        = models.CharField(max_length=10)
    car_tempreture      = models.CharField(max_length=4)
    car_engine_load     = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
    Latitude            = models.CharField(max_length=100,blank=True,null=True)
    Longitude           = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        verbose_name_plural = "Car"

    def __str__(self):
        return f"Car - ({self.car_id})"


class Car_Diagnostic(models.Model):
    diagnostic_for_car      = models.ForeignKey(Car, on_delete=models.CASCADE,null=True)
    diagnostic_sarial       = models.CharField(max_length=7)
    diagnostic_error_type   = models.TextField()

    class Meta:
        verbose_name_plural = "Car Diagnostic"

    def __str__(self):
        return f"diagnostic with sarial (_ {self.diagnostic_sarial} _) for car with id (_ {self.diagnostic_for_car.car_id} _)"


class MCVUser(models.Model):
    user                    = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=100)
    image                   = models.ImageField(upload_to='mcv_user/')
    mobile                  = models.CharField(max_length=20)
    Latitude                = models.CharField(max_length=100,blank=True,null=True)
    Longitude               = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        verbose_name_plural = 'MCV USER'
        
    def __str__(self):
        return self.full_name
    
class Driver(models.Model):
    classes                 = ["Driving safe","Texting right","Talk with right","Texting left","Talk with left","Turn on radio","Drinking","look behind","hair and makeup","talking passenger",]
    DRIVER_ACTION           = ((i,i) for i in classes)
    user                    = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name               = models.CharField(max_length=100)
    image                   = models.ImageField(upload_to='mcv_user/')
    mobile                  = models.CharField(max_length=20)
    drive_car               = models.OneToOneField(Car, on_delete=models.CASCADE , null=True)
    driver_action           = models.CharField(max_length=100, choices=DRIVER_ACTION, default="Driving safe")

    class Meta:
        verbose_name_plural = "Driver"

    def __str__(self):
        return f"Driver (_ {self.full_name} _) drive car with id (_ {self.drive_car.car_id} _) "
