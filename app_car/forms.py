from django import forms

from app_car.models import Contact,Booking,Review


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
        # fields = (
        #     "name", 
        #     "phone_number", 
        #     "email",
        #     "pickup_type",
        #     "payment_type",
        #     "journey_date",
        #     "journey_time",
        #     "passenger_number",
        #     "flight_number",
        #     "main_luggage",
        #     "hand_luggage",
        #     "pickup_address",
        #     "destination_address",
        #     "is_return_journey",
        #     "return_journey_date",
        #     "return_journey_time",
        #     "return_passenger_number",
        #     "return_flight_number",
        #     "return_main_luggage",
        #     "return_hand_luggage",
        #     "return_pickup_address",
        #     "return_destination_address",
        #     "booking_note",
        #     "service_type",
        #     "promo_code",
        #     "privacy_agree",
        #     "terms_agree"
        # ) 


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','email', 'content', 'rating']
        
        
