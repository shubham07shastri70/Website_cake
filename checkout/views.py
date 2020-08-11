from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from main_page.forms import PaymentForm

# Import Payu from Paywix
from paywix.payu import Payu

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

# Create Payu Object for making transaction
# The given arguments are mandatory
payu = Payu(merchant_key, merchant_salt, surl, furl, mode)


# Payu checkout page
@csrf_exempt

def payu_checkout(request):

        
        
        # The dictionary data  should be contains following details
        if request.method == 'POST':
            print('posteddddd')
            form=PaymentForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                print(form.errors)
        # Making Checkout form into dictionary
            data = {k: v[0] for k, v in dict(request.POST).items()}
            amount=request.POST.get('amount')
            name=request.POST.get('name')
            print(name)
            msg=request.POST.get('message')
            weight=request.POST.get('cake_weight')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            cake_name=request.POST.get('cake_title')
            data = { 'amount': amount, 
                'firstname': name, 
                'email': 'bakedbyheart@gmail.com',
                'phone': phone, 'productinfo': 'test', 
                'message_on_cake':msg,
                'weight_in_pound':weight,
                'address':address,
                'title':cake_name,
                
            }
            
            # No Transactio ID's, Create new with paywix, it's not mandatory
            # Create your own
            # Create transaction Id with payu and verify with table it's not existed
            txnid = payu.generate_txnid()
            data.update({"txnid": txnid})
            payu_data = payu.transaction(**data)
            return render(request, 'payu_checkout.html', {"posted": payu_data})

@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return render(request,'success.html')

@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return render(request,'failure.html')
