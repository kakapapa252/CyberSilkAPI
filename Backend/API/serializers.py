from rest_framework import serializers
import datetime
import pytz

from .models import (
    Category,
    Product,
    ColorOptions,
    SizeOptions,
    PhoneTypeOptions
    )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  ("id", "name", "description", "image", "icon")


#options ------------

class ColorOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorOptions
        fields =  ("id", "name", "hashCode")
        
class SizeOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeOptions
        fields =  ("id", "name", "sizeCode")

class PhoneTypeOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneTypeOptions
        fields =  ("id", "name", "modelCode")


class ProductSerializer(serializers.ModelSerializer):
    colorOptions = ColorOptionsSerializer(read_only=True, many=True)
    sizeOptions = SizeOptionsSerializer(read_only=True, many=True)
    phoneTypeOptions = PhoneTypeOptionsSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields =  ("id", "name", "description", "image", "basePrice", "printPrice", "discountPrice",
                    "colorOptions", "sizeOptions", "phoneTypeOptions", "inStock")


