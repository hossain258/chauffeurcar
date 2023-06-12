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
        verbose_name_plural = "Courses"



    def __str__(self):
        return self.title