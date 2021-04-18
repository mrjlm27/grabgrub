from django.db import models
# models.ForeignKey(Supplier, on_delete = models.CASCADE)
# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    created_at = models.DateTimeField(blank = True, null = True)
    objects = models.Manager()

    def getName(self):
        return self.name
    
    def getDesc(self):
        return self.description

    def getPrice(self):
        return self.price

    def __str__(self):
        return str(self.pk)+": "+self.name+" - "+str(self.price)+", "+self.description+" created at: "+str(self.created_at)

class Customer(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    objects = models.Manager()


    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def __str__(self):
        return str(self.pk)+": "+self.name+" - "+self.address+", "+self.city

class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True,blank = True, null = True)
    mode_payment = models.CharField(max_length=300)
    cust_order = models.ForeignKey(Customer, on_delete = models.CASCADE)
    objects = models.Manager()

    def getMode(self):
        return self.mode_payment


    def __str__(self):
        return str(self.pk)+": "+self.cust_order.name+", "+self.cust_order.address+", "+self.cust_order.city+", "+self.mode_payment+", ordered at "+str(self.ordered_at)


class OrderLine(models.Model):
    ORD = models.ForeignKey(Order, on_delete = models.CASCADE)
    food = models.ForeignKey(Food, on_delete = models.CASCADE)
    quantity = models.FloatField()
    objects = models.Manager()

    def getQuantity(self):
        return self.quantity

    def solver(self):
        total = self.quantity * self.food.price
        return total

    def __str__(self):
        return str(self.pk)+": "+str(self.ORD.pk)+" - "+self.food.name+str(self.quantity)
    
    