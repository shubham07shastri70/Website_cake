from django.shortcuts import render
from  main_page.models import *
from  main_page.forms import OrderForm
from  main_page.forms import PaymentForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views import View
from django.http import HttpResponse


class PaymentNet(View):
    
    def get(self, request):
        form=PaymentForm()
        title=request.GET.get('title')
        base=request.GET.get('price')
        price=base
        if request.method == 'GET':
            return render(request,'payment.html',context={'title':title,'price':price,'form':form})

    def post(self, request):
        form=PaymentForm()
        title=request.GET.get('title')
        base=request.GET.get('price')
        price=base
        if request.method=='POST':
            print('post')
            form=PaymentForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                print(form.errors)
        return render(request,'payment.html',context={'title':title,'price':price,'form':form})

class CreateNetwork(View):
    
    def get(self, request):
        form=OrderForm()
        Birthday =BirthdayTable.objects.all()
        Anniversary=AnniversaryTable.objects.all()
        Special=SpecialTable.objects.all()
        Insta=InstaTable.objects.all()
        if request.method == 'GET':
            return render (request, 'index.html', context={'form':form,'bd' : Birthday,'an':Anniversary,'spl':Special,'ins':Insta})

    def post(self, request):
        form=OrderForm()
        Birthday =BirthdayTable.objects.all()
        Anniversary=AnniversaryTable.objects.all()
        Special=SpecialTable.objects.all()
        Insta=InstaTable.objects.all()
        if request.method=='POST':
            print('post')
            form=OrderForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                print('invalid fields')
        return render (request, 'index.html', context={'form':form,'bd' : Birthday, 'an':Anniversary,'spl':Special,'ins':Insta})


