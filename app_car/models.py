from django.db import models

# Create your models here.


class Basemodel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True, )
    class Meta:
        abstract = True
        ordering = ("-created_at",)


class Contact(Basemodel):
    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=155, blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(max_length=1200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    


class Services(Basemodel):
    title=models.CharField(max_length=120, blank=True, null=True)
    headline=models.CharField(max_length=500, blank=True, null=True)
    service_img=models.ImageField(upload_to='services', blank=True, null=True)

    class Meta:
        verbose_name_plural = "services"



    def __str__(self):
        return self.title
    


class Booking(Basemodel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    payment_type = models.IntegerField(default=0)
    journey_date = models.DateField(auto_now=False, auto_now_add=False)
    journey_time = models.DateField(auto_now=False, auto_now_add=False)
    passenger_number = models.IntegerField(default=0)
    flight_number = models.IntegerField(default=0)
    main_luggage = models.IntegerField(default=0)
    hand_luggage = models.IntegerField(default=0)
    pickup_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)

    is_return_journey = models.BooleanField(default=False)
    return_journey_date = models.DateField(auto_now=False, auto_now_add=False)
    return_journey_time = models.DateField(auto_now=False, auto_now_add=False)
    return_passenger_number = models.IntegerField(default=0)
    return_flight_number = models.IntegerField(default=0)
    return_main_luggage = models.IntegerField(default=0)
    return_hand_luggage = models.IntegerField(default=0)
    return_pickup_address = models.CharField(max_length=200)
    return_destination_address = models.CharField(max_length=200)

    booking_note = models.TextField(max_length=1000)

    service_type = models.IntegerField(default=0)  # Standered = 1, Premium = 2
    promo_code = models.CharField(max_length=20, null=True, blank=True)

    privacy_agree = models.BooleanField(default=False)
    terms_agree = models.BooleanField(default=False)


    def __str__(self):
        return self.name