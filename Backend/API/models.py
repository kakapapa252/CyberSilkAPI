from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class UserDevice(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    token = models.CharField(max_length=200, blank=False, null=False, unique=True)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.token}"
    
class SessionReport(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    userDevice = models.ForeignKey(UserDevice, on_delete=models.CASCADE, null=True, blank=True)
    createDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    

class ColorOptions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    hashCode = models.CharField(max_length=20, blank=False, null=False)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} :: {self.hashCode}"
    
    
class SizeOptions(models.Model):
    id = models.AutoField(primary_key=True, unique=True) 
    name = models.CharField(max_length=200, blank=False, null=False)
    sizeCode = models.CharField(max_length=20, blank=False, null=False)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} :: {self.sizeCode}"
    
    
class PhoneTypeOptions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    modelCode = models.CharField(max_length=20, blank=False, null=False)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    

class GenDesign(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    userDevice = models.ForeignKey(UserDevice, on_delete=models.SET_NULL, null=True, blank=True)
    prompt = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prompt}"
    

class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    basePrice = models.DecimalField(default=0, decimal_places=2, blank=False, null=False, max_digits=10)
    printPrice = models.DecimalField(default=0, decimal_places=2, blank=False, null=False, max_digits=10)
    discountPrice = models.DecimalField(default=0, decimal_places=2, blank=False, null=False, max_digits=10)
    inStock = models.BooleanField(default=True)
    
    #colorOtions = models.JSONField(null=True, blank=True)
    #sizeOptions = models.JSONField(null=True, blank=True)
    #phoneTypeOptions = models.JSONField(null=True, blank=True)
    colorOptions = models.ManyToManyField(ColorOptions, blank=True)
    sizeOptions = models.ManyToManyField(SizeOptions, blank=True)
    phoneTypeOptions = models.ManyToManyField(PhoneTypeOptions, blank=True)


    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} :: {self.category}"
    

class Cart(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    userDevice = models.ForeignKey(UserDevice, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    design = models.ForeignKey(GenDesign, on_delete=models.SET_NULL, null=True, blank=True)

    createDateTime = models.DateTimeField(auto_now_add=True)
    updateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"