from django import views
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from product.models import *
from .serlizer import *



@api_view(['GET'])
def getall(request):
    products = product.objects.all()
    return Response({"msg":"found","data":ProductSerializer(products,many=True).data})


@api_view(['GET'])
def getbyid(request,pk):
    try:
        products = product.objects.get()
    except:
        return JsonResponse({'error':'not found'},status=404)
    else:
        return Response({"msg":"found","data":ProductSerializer(products).data},status=200)

@api_view(['POST'])
def add(request):
    product = ProductSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response(product.data, status=201)
    else:
        return Response(product.errors,status=400)

@api_view(["DELETE"])
def delete(request, pk):
    products=product.objects.filter(id=pk)
    if(len(products)>0):
        product.delete()
        return Response(data={'msg':'Product deleted'})
    return Response({'msg':'product not found'})

@api_view(['GET','PUT'])
def update(request,pk):
    products = product.objects.filter(id=pk).first()
    if products:
        productdata = ProductSerializer(instance=products,data=request.data)
        if productdata.is_valid():
            productdata.save()
            return Response(data=productdata.data,status=200)
        return Response(productdata.errors,status=400)
