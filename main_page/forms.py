from django import forms
from main_page.models import AnniversaryTable,BirthdayTable,InstaTable,OrderTable,SpecialTable,PaymentTable
from bootstrap_modal_forms.forms import BSModalForm
from db_file_storage.form_widgets import DBAdminClearableFileInput
from db_file_storage.form_widgets import DBClearableFileInput
from django.contrib import admin
from main_page.models import OrderTable

class BirthdayForm(forms.ModelForm):
    class Meta():
        model=BirthdayTable
        fields='__all__'

class AnniversaryForm(forms.ModelForm):
    class Meta():
        model=AnniversaryTable
        fields='__all__'

class SpecialForm(forms.ModelForm):
    class Meta():
        model=SpecialTable
        fields='__all__'

class InstaForm(forms.ModelForm):
    class Meta():
        model=InstaTable
        fields='__all__'

class OrderForm(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'type':'text',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Name'
        }
    ))
    Email=forms.CharField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'type':'email',
            'placeholder':'Email',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
        }
    ))
    Phone=forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'type':'tel',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Phone'
        }
    ))
    Details=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'type':'text',
            'style':'height: 100px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Tell us a bit about your requirements'
        }
    ))
    class Meta():
        model=OrderTable
        fields=('Name','Email','Phone','Details')
        

class PaymentForm(forms.ModelForm):
    cake_title=forms.HiddenInput()
    amount=forms.HiddenInput()
    name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control col-12 col-lg-5',
            'type':'text',
            'name':'name',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Name'
        }
    ))
    message=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control col-12 col-lg-6',
            'type':'text',
            'name':'message',
            'placeholder':'Message On Cake',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
        }
    ))
    phone=forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'form-control col-12 col-lg-6',
            'type':'tel',
            'name':'phone',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Phone'
        }
    ))
    address=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'type':'text',
            'name':'address',
            'style':'height: 100px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Delivery Address'
        }
    ))
    class Meta():
        model=PaymentTable
        fields=('cake_weight','message','name','phone','address','amount','cake_title')
        
