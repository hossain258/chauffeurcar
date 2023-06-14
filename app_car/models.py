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
    thumbnail_image=models.ImageField(upload_to='services', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "services"



    def __str__(self):
        return self.title
    


class Booking(Basemodel):


    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('action_pending', 'Action Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    PICKUP_TYPE_CHOICES =(
        ('Airport', 'Airport'),
        ('Railway', 'Railway'),
        ('Seaport', 'Seaport'),
        ('Other address', 'Other address'),

    )

    PAYMENT_TYPE_CHOICES= (

        ('Cash', 'Cash'),
        ('pay in the car by card', 'pay in the car by card'),
        ('Pay in advance', 'Pay in advance'),
        

    ) 

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    pickup_type = models.CharField(max_length=30 ,choices=PICKUP_TYPE_CHOICES, default='Airport')
    payment_type = models.CharField(max_length=30, choices=PAYMENT_TYPE_CHOICES, default='Cash')
    journey_date = models.DateField(blank=True, null=True)
    journey_time = models.TimeField(blank=True, null=True)
    passenger_number = models.IntegerField(default=0)
    flight_number = models.CharField(max_length=100, blank=True, null=True)
    main_luggage = models.IntegerField(default=0)
    hand_luggage = models.IntegerField(default=0)
    pickup_address = models.CharField(max_length=200, blank=True, null=True)
    destination_address = models.CharField(max_length=200, blank=True, null=True)

    is_return_journey = models.IntegerField(default=0, blank=True, null=True)
    return_journey_date = models.DateField(blank=True, null=True)
    return_journey_time = models.TimeField(blank=True, null=True)
    return_passenger_number = models.IntegerField(default=0)
    return_flight_number = models.CharField(max_length=100, blank=True, null=True)
    return_main_luggage = models.IntegerField(default=0)
    return_hand_luggage = models.IntegerField(default=0)
    return_pickup_address = models.CharField(max_length=200, blank=True, null=True)
    return_destination_address = models.CharField(max_length=200, blank=True, null=True)

    booking_note = models.TextField(max_length=1000, blank=True, null=True)

    service_type = models.IntegerField(default=0)  # Standered = 1, Premium = 2
    promo_code = models.CharField(max_length=20, null=True, blank=True)

    privacy_agree = models.IntegerField(default=0, blank=True, null=True)
    terms_agree = models.IntegerField(default=0, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return self.name