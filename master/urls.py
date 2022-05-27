from django.urls import path
from master.views import hello_world, HomeView, about_us_view,contact_us_view,AboutUsView,ContactUsView,ContactedList,ContactUsSendReply,ContactUsReply

urlpatterns=[
    path("",HomeView.as_view(),name="home"),
    path("hello_world",hello_world,name="hello_world"),
    #path('about_us',about_us_view,name='about_us'),
    path('about_us',AboutUsView.as_view(),name='about_us'),
    #path('contact_us',contact_us_view,name="contact_us")
    path('contact_us',ContactUsView.as_view(),name='contact_us'),
    path('contactedemail',ContactedList.as_view(),name='contactedemail'),
    path("contactus/<int:pk>/send", ContactUsSendReply.as_view(), name='contactus_send_reply'),
    path("contactus/<int:pk>/reply", ContactUsReply.as_view(), name='contactus_view_reply'),

]