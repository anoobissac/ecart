
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView,View,DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from product.models import ProductModel,CategoryModel
from master.forms import ContactForm
from master.models import ContactUs

# Create your views here.
#def home_view(request):
#    template_name='master/home.html'
#    context={
#        'title':'home'
#    }
#    return render(request,template_name,context)

#class based view

class HomeView(TemplateView) :
    template_name='master/home.html'
    extra_context={
         'title':'home',
         'products' : ProductModel.objects.all(), #displaying product in home page
         'category':CategoryModel.objects.all()
    }

def hello_world(request):
    return HttpResponse("<h1> Hello World</h1>")

def about_us_view(request):
    template_name='master/about_us.html'
    context={
        'title':'About Us'
    }
    return render(request,template_name,context)

class AboutUsView(TemplateView):
    template_name="master/about_us.html"
    extra_context={
        'title':'About Us',
        'category':CategoryModel.objects.all()
    }

def contact_us_view(request):
    template_name='master/contact_us.html'
    context={
        'title':'Contact Us'
    }
    return render(request,template_name,context)

class ContactUsView(View):
    template_name='master/contact_us.html'
    form_class= ContactForm
  
    def get (self, request):
        context={
        'title':'Contact Us',
        'form':self.form_class
    }
        return render (request,self.template_name,context)
    def post(self,request):
        form =self.form_class(request.POST)
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return redirect(reverse_lazy('contact_us'))


    def form_valid(self,form):
        data= form.cleaned_data
        from_email=settings.EMAIL_HOST_USER
        to_email=data['email']
        name=data['name']
        subject=data['subject']
        message=data['message']


        contact_obj=ContactUs.objects.create(
            name=name,
            email=to_email,
            subject=subject,
            message=message
        )

        #sending email
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[to_email]
        )
        print("Mail sent successfully!!")
        
    def form_invalid(self,form):
        context={
                "form":form
        }
        return render(self.request,self.template_name,context)

class ContactedList(View):
    template_name='master/contactedemail.html'
    def get(self,request):
        context={
            "emails":ContactUs.objects.all()
        }
        return render (request,self.template_name,context)

class ContactUsSendReply(View):
    template_name = 'master/contactus/send_reply.html'
    form_class = ContactForm
    def get(self,request, pk):
        context={
            'form':self.form_class
        }
        return render(request,self.template_name,context)
    
    def post(self, request, pk):
        form = self.form_class(request.POST)
        self.object = ContactUs.objects.get(id=pk)
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return redirect(reverse_lazy('contactedemail'))
        

    def form_valid(self, form):
        data = form.cleaned_data
        from_email = settings.EMAIL_HOST_USER
        to_email = self.object.email
        name = data['name']
        subject = data['subject']
        message = data['message']
        
        # sending email
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_email, 
            recipient_list=[to_email]
            )

        print("Mail sent successfully!!")

        self.object.reply = message
        self.object.is_replied = True
        self.object.save()

    def form_invalid(self, form):
        context = {
            "form" : form
        }
        return render(self.request, self.template_name, context)


class ContactUsReply(DetailView):
    template_name = 'master/contactus/view_reply.html'
    model = ContactUs