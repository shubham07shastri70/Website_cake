from django.conf.urls import url
from django.urls import path
from main_page import views

urlpatterns = [
    path('payment/',views.PaymentNet.as_view()),
    url(r'^$',views.CreateNetwork.as_view(),name='home'),
    
    
]
