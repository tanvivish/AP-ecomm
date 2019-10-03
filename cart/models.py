from django.db import models

# Create your models here.


class product(models.Model):
    product_ID = models.IntegerField(primary_key=True)
    prodcut_name = models.CharField(max_length = 200, blank = True)
    category = models.CharField(max_length = 200, blank = True)
    product_stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    product_description = models.CharField(max_length = 300, default = 'Null')
    cart = models.CharField(max_length = 1, default = "0")
    quantity = models.IntegerField(default = 0)

    def __unicode__(self):
        return str(self.product_ID)

class transaction(models.Model):
    transaction_ID = models.IntegerField(default = 0)
    product_ID = models.ForeignKey(product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    
    class Meta:
        unique_together = (('transaction_ID', 'product_ID'),)
        
class order(models.Model):
    order_ID = models.AutoField(primary_key = True)
    transaction_ID = models.ForeignKey(transaction, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, blank = True)
    email = models.CharField(max_length = 200, blank = True)
    mobile = models.CharField(max_length = 200, blank = True)
    address = models.CharField(max_length = 200, blank = True)
    method = models.CharField(max_length = 200, blank = True)
    




