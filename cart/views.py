from django.shortcuts import render
from django.http import HttpResponse
from .models import product, transaction,order
from django.template import loader

from .forms import PaymentInfo

def detail(request, product_id):
    products = product.objects.all().filter(product_ID = product_id)[0]
    template = loader.get_template('cart/templates/detail.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))
    
def index(request):
    products = product.objects.all()
    template =  loader.get_template('cart/index.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def equipment(request):
    products = product.objects.all().filter(category = "Equipment")
    template = loader.get_template('cart/equipment.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def shoes(request):
    products = product.objects.all().filter(category = "Shoes")
    template = loader.get_template('cart/templates/shoes.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def clothing(request):
    products = product.objects.all().filter(category = "Clothing")
    template = loader.get_template('ecommerce/fashion.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def createpost(request, product_id):
        products = product.objects.get(product_ID = product_id)
        products.cart = "1"
        products.quantity = products.quantity + 1
        products.save(update_fields=['cart'])
        products.save(update_fields=['quantity'])
        template = loader.get_template('cart/added_cart.html')
        context = {
            'products': products,
        }
        return HttpResponse(template.render(context, request))

def cart(request):
    products = product.objects.all().filter(cart = "1")
    template = loader.get_template('cart.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def checkout(request):
    products = product.objects.all().filter(cart = "1")
    context = {
        'products': products,
    } 
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render(context, request))

def payment(request):
    template = loader.get_template('cart/payment.html')
    if(request.method == "GET"):
        form = PaymentInfo()
        context = {'form': form}
        return HttpResponse(template.render(context, request))
    
    else:
        form = PaymentInfo(request.POST)
        if form.is_valid():
            products = product.objects.all().filter(cart = "1")
            ID = len(transaction.objects.all()) + 1
            for p in products:
                t = transaction(transaction_ID = ID, product_ID = p, quantity = p.quantity)
                t.save()
                s = shipping(transaction_ID = t)
                s.save()
                p.cart = "0"
                p.product_stock = int(p.product_stock) - int(p.quantity)
                p.quantity = 0
                p.save(update_fields = ['product_stock'])
                p.save(update_fields=['cart'])
                p.save(update_fields=['quantity'])
            instance = form.save(commit=False)
            instance.transaction_ID = t
            instance.save()
        template = loader.get_template('cart/complete.html')
        return HttpResponse(template.render({}, request))
    
def completepayment(request):
    template = loader.get_template('cart/complete.html')
    return HttpResponse(template.render({}, request))

def search(request):     
    if(request.method == 'POST'):      
        search = request.POST.get('search')      
        status = product.objects.all().filter(product_name = search)
        context = {
            "product":product
        }
        template = loader.get_template('cart/templates/search.html')
        return template.render(context, request)
    else:
        return render(request,"search.html",{})