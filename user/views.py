from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from user.models import ProfileModel
from django.urls import reverse_lazy
from user.forms import UserForm
from user.forms import ProfileForm, UserForm
from user.models import ProfileModel


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

class DashboardView(View):
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



