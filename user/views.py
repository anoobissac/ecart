import requests
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View,RedirectView
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin


from user.models import ProfileModel
from user.forms import UserForm
from user.forms import ProfileForm, UserForm,LoginForm







# Create your views here.
class UserCreateView(CreateView):
    template_name="users/create.html"
    model=ProfileModel
    #fields = ['name','price','image','description','category','unit']
    form_class=UserForm
    success_url = reverse_lazy('user_list')


class UserListView(ListView):
    template_name='users/list.html'
    model=ProfileModel

class UserDetailView(DetailView):
    template_name='users/detail.html'
    model=ProfileModel

class UserUpdateView(UpdateView):
    template_name="users/update.html"
    model=ProfileModel
    #fields = ['name']
    form_class=ProfileForm
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    template_name="users/delete.html"
    model=ProfileModel    
    success_url = reverse_lazy('user_list')

# Create your views here.
# Profile
class ProfileView(DetailView):
    template_name = "profile/profile.html"
    model = ProfileModel

    def get_queryset(self):
        queryset = ProfileModel.objects.get(user=self.request.user)
        return queryset

class ProfileCreateView(CreateView):
    template_name = 'users/profile/create.html'
    form_class = ProfileForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

# User
class UserRegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserForm
    success_url = reverse_lazy('home')


# class DashboardView(TemplateView):
#     template_name = 'user/dashboard.html'

class DashboardView(LoginRequiredMixin, View):
    template_name = 'users/dashboard.html'

    def get(self, request):
        profile = self.get_queryset()
        context = {
            'profile' : profile
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass

    def get_queryset(self):
        queryset = ProfileModel.objects.filter(user=self.request.user).first()
        return queryset

class LoginView(View):
    template_name="registration/login.html"
    form_class=LoginForm
    def get (self,request):
        context={
            "form": self.form_class()
        }
        return render(request,self.template_name,context)

    def post (self,request):
        form =self.form_class(request.POST)
        
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return redirect(reverse_lazy('dashboard'))

    def form_valid(self,form):
        
        user=None
        data=form.cleaned_data
        username=data['username']
        password=data['password']
        recaptcha_response = self.request.POST.get("g-recaptcha-response")
        values={
            'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response':recaptcha_response
        }
        url=settings.GOOGLE_RECAPTCHA_VERIFY_URL
        data=requests.post(url,data=values).json()
        if data['success']:
            user=authenticate(self.request,username=username,password=password)
        if user is None:
            return self.form_invalid(form)
        login(self.request,user)


    def form_invalid(self,form):
        context={
            'form':form
        }
        return render(self.request,self.template_name,context)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse_lazy('home'))