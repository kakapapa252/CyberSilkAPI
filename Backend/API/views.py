from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    UserDevice,
    SessionReport,
    Category,
    Product
)

from .serializers import (
    CategorySerializer,
    ProductSerializer
)

from rest_framework import status


@api_view(["POST"])
def tokenValidation(request):
    try:
        token = request.data.get("deviceToken")
        userDevice = UserDevice.objects.get_or_create(token=token)[0]
        print(userDevice.token)
        SessionReport.objects.create(userDevice = userDevice)
        return Response(status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def categoryView(request):
    try:
        categoryList = Category.objects.all()
        serializer = CategorySerializer(categoryList, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def productListView(request, cat_id):
    try:
        category = Category.objects.get(id=cat_id)
        productList = Product.objects.filter(category=category)
        serializer = ProductSerializer(productList, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def productView(request, prod_id):
    try:
        product = Product.objects.get(id=prod_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)