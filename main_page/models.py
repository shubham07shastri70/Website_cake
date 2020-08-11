from django.db import models
# Create your models here.
class BirthdayTable(models.Model):
    cake_title=models.CharField(max_length=128)
    cake_price=models.CharField(max_length=512)
    cake_photo=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cake_title

class AnniversaryTable(models.Model):
    cake_title=models.CharField(max_length=128)
    cake_price=models.CharField(max_length=512)
    cake_photo=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cake_title

class SpecialTable(models.Model):
    cake_title=models.CharField(max_length=128)
    cake_price=models.CharField(max_length=512)
    cake_photo=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cake_title

class InstaTable(models.Model):
    cake_photo=models.ImageField(upload_to='images/')

    def __str__(self):
        return 'success'

class OrderTable(models.Model):
    Name=models.CharField(max_length=128)
    Phone=models.CharField( max_length=128)
    Details=models.CharField(max_length=1024,null=True)
    Email=models.EmailField( max_length=254,null=True)
    
    
    

    def __str__(self):
        return self.Name


class PaymentTable(models.Model):
    pound=(
        (1,'Select cake weight in pound'),
        (1,'1 pound'),
        (2,'2 pound'),
        (3,'3 pound'),
        (4,'4 pound'),
        (5,'5 pound'),
    )
    cake_title=models.CharField(max_length=100,null=False)
    name=models.CharField(max_length=128)
    phone=models.CharField( max_length=128)
    address=models.CharField(max_length=1024,null=True)
    message=models.CharField(max_length=1024,null=True)
    cake_weight=models.IntegerField(max_length=10,choices=pound,default=1)
    amount=models.CharField(max_length=10)
    
    
    
    

    def __str__(self):
        return self.name