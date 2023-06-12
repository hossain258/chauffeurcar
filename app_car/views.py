from django.shortcuts import render
from django.views.generic import TemplateView
from app_car.models import Contact
from app_car.forms import ContactForm,BookingForm
from django.http import JsonResponse


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # service_list = Service.objects.filter(is_featured=True)

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

# def booking(request):
#     diction ={}
#     return render(request,'booking-passenger.html', context=diction)

def services(request):
    dict={}
    return render(request,'services.html', context=dict)



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
        form = BookingForm(request.POST)
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
    
    form=BookingForm()
        
    return render(request, 'booking-passenger.html', {'form':form})