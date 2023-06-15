from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from app_car.models import Contact,Services, Booking,Review
from app_car.forms import ContactForm,BookingForm,ReviewForm
from django.http import JsonResponse
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['services'] = Services.objects.filter(is_featured=True)
        context['form'] =ContactForm
        print(context['services'])
        return context
    

def about(request):
    diction ={}
    return render(request,'about.html', context=diction)

def gallery(request):
    diction ={}
    return render(request,'gallery.html', context=diction)

def fleet(request):
    diction ={}
    return render(request,'fleet.html', context=diction)

def faq(request):
    diction ={}
    return render(request,'faq.html', context=diction)

def privacy(request):
    diction ={}
    return render(request,'privacy.html', context=diction)


def servicedetails(request):
    diction ={}
    return render(request,'servicedeatils.html', context=diction)


def pricetable(request):
    diction ={}
    return render(request,'pricing.html', context=diction)





class serviceListView(ListView):
    model = Services
    template_name = "services.html"
    paginate_by = 6
    context_object_name='services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
           
        return context



def contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        # name = request.POST['name']
        # email = request.POST['email']
        # phone_number = request.POST.get('phone_number')
        # message = request.POST['message']
        # values = Contact(name=name, email=email,phone_number=phone_number,message=message)        
        form.save()
        #  success=('the form submited successfully')
        # messages.success(request,"The message has been successfully submitted !!")
        # send_email = EmailMessage(
        #     f"""  message from ICTINEX """,
        #     f"""Sender:{name}""",
        #     # from
        #     f'{EMAIL_HOST_USER}',
        #     # to
        #     [email],
        #     reply_to=[email],
        #     )
        # send_email.send()
        # messages.success(request,"The message has been successfully submitted !!")
        return JsonResponse({'status':'The form submitted successfully'})
    
    form=ContactForm()
        
    return render(request, 'contact.html', {'form':form})



def booking(request):
    
    if request.method == "POST":
        # form = BookingForm(request.POST) 

        if request.POST.get('is_return_journey', False) == 1:
            values = Booking(
                name = request.POST['name'],
                phone_number = request.POST['phone_number'],
                email = request.POST['email'],
                pickup_type = request.POST['pickup_type'],
                payment_type = request.POST['payment_type'],
                journey_date = request.POST['journey_date'],
                journey_time = request.POST['journey_time'],
                passenger_number = request.POST['passenger_number'],
                flight_number = request.POST['flight_number'],
                main_luggage = request.POST['main_luggage'],
                hand_luggage = request.POST['hand_luggage'],
                pickup_address = request.POST['pickup_address'],
                destination_address = request.POST['destination_address'],
                is_return_journey = request.POST.get('is_return_journey', False),
                
                return_journey_date = request.POST['return_journey_date'],
                return_journey_time = request.POST['return_journey_time'],
                return_passenger_number = request.POST['return_passenger_number'],
                return_flight_number = request.POST['return_flight_number'],
                return_main_luggage = request.POST['return_main_luggage'],
                return_hand_luggage = request.POST['return_hand_luggage'],
                return_pickup_address = request.POST['return_pickup_address'],
                return_destination_address = request.POST['return_destination_address'],

                booking_note = request.POST['booking_note'],
                service_type = request.POST['service_type'],
                promo_code = request.POST['promo_code'],
                privacy_agree = request.POST.get('privacy_agree', False),
                terms_agree = request.POST.get('terms_agree', False),
            )     
        else:
             values = Booking(
                name = request.POST['name'],
                phone_number = request.POST['phone_number'],
                email = request.POST['email'],
                pickup_type = request.POST['pickup_type'],
                payment_type = request.POST['payment_type'],
                journey_date = request.POST['journey_date'],
                journey_time = request.POST['journey_time'],
                passenger_number = request.POST['passenger_number'],
                flight_number = request.POST['flight_number'],
                main_luggage = request.POST['main_luggage'],
                hand_luggage = request.POST['hand_luggage'],
                pickup_address = request.POST['pickup_address'],
                destination_address = request.POST['destination_address'],
                is_return_journey = request.POST.get('is_return_journey', False),
                booking_note = request.POST['booking_note'],
                service_type = request.POST['service_type'],
                promo_code = request.POST['promo_code'],
                privacy_agree = request.POST.get('privacy_agree', False),
                terms_agree = request.POST.get('terms_agree', False),
            )  
        values.save()
        form=BookingForm()
        messages.success(request,"The booking request has been successfully submitted . Please wait for confirmation email !! or Call us on 0772546355")
        # return JsonResponse({'status':'The form save successfully'})

        # form = BookingForm(request.POST)
        # print(form.is_valid())
        # print('faisal ==========')
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse({'status':'The form save successfully'})
            # print(form)
        # name = request.POST['name']
        # # print(name)
        # # exit
        # email = request.POST['email']
        # phone_number = request.POST.get('phone_number')
        # message = request.POST['message']
        # values = Contact(name=name, email=email,phone_number=phone_number,message=message)        
        # form.save()
        # success=('the form submited successfully')
        # messages.success(request,"The message has been successfully submitted !!")
        # send_email = EmailMessage(
        #     f"""  message from ICTINEX """,
        #     f"""Sender:{name}""",
        #     # from
        #     f'{EMAIL_HOST_USER}',
        #     # to
        #     [email],
        #     reply_to=[email],
        #     )
        # send_email.send()
        # messages.success(request,"The message has been successfully submitted !!")
    
    form=BookingForm()
        
    return render(request, 'booking-passenger.html', {'form':form})



def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # review.user = request.user
            review.save()
            messages.success(request, 'Review created successfully!')
            return redirect('reviews')
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(is_published=True)
    return render(request, 'reviewform.html', {'form': form, 'reviews': reviews})