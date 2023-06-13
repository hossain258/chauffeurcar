from django import forms

from app_car.models import Contact,Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone_number", "message")

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email Address'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type Your message'})
        }



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__' 
        exclude = ('created_at',)
        