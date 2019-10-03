from django import forms
from .models import order

#Quantity = [tuple([x,x]) for x in range(1,32)]
#class CartForm(forms.Form):
#    quantity = forms.IntegerField(label='Quantity')


class PaymentInfo(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    mobile = forms.CharField(label='Mobile No.', max_length=100)
    email = forms.EmailField(label = 'Email ID')
    address = forms.CharField(label='Shipping Address', max_length=100)
    method = forms.CharField(label='Payment Method' , max_length=100)
    
    class Meta:
        model = order
        fields = ('name', 'mobile', 'email', 'address', 'method')