from django.urls import path,include
from user.views import UserDetailView,UserListView,UserCreateView,UserDeleteView,UserUpdateView, DashboardView, ProfileCreateView, UserRegistrationView, ProfileView

urlpatterns=[
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/create', ProfileCreateView.as_view(), name='profile_create'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/',UserCreateView.as_view(),name="user_create"),
    path("list/",UserListView.as_view(),name="user_list"),
    path("<int:pk>/detail/",UserDetailView.as_view(),name="user_detail"),
    path('<int:pk>/update/',UserUpdateView.as_view(),name='user_update'),
    path('<int:pk>/delete/',UserDeleteView.as_view(),name='user_delete')
    ]