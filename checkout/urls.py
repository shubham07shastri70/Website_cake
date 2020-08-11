from django.conf.urls import url
from django.urls import path
from checkout import views

urlpatterns = [
    path('paymentpg',views.payu_checkout,name=""),
    
    
    
    
]