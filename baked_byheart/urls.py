"""baked_byheart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import checkout
from main_page import views
from checkout import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^files/', include('db_file_storage.urls')),
    path('',include('main_page.urls')),
    path('checkout/',include('checkout.urls')),
    path('success/',checkout.views.payu_success,name=""),
    path('failure/',checkout.views.payu_failure,name=""),
    path('admin/', admin.site.urls),
]
if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)