#from django.shortcuts import render
from rest_framework import serializers
from rest_framework.fields import FileField
#from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


@api_view(['GET'])
def showAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully !')


@api_view(['GET'])
def showAllCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()

    return Response('Items delete successfully !')


"""class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    Filter_Fields = {'category', }
    search_fields = {'name', }"""
