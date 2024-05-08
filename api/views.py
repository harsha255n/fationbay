
from django.shortcuts import render
from rest_framework.views import APIView
from api.serializer import Signup
from rest_framework.response import Response 
from rest_framework.viewsets import ViewSet
from api.serializer import ProductSerilizer
from Store.models import Product
from rest_framework.response import Response
from rest_framework import status
"""VIESET """
# vieset ->> create  list retrive distroy  update
# automatically created urls 

# Create your views here.
class Signupview(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Signup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class product_view(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Product.objects.all()
        serializer=ProductSerilizer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def create(self,request,*args,**kwargs):
        serializer=ProductSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=ProductSerilizer(qs)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Product.objects.get(id=id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Product.objects.get(id=id)
        serializer=ProductSerilizer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
        







        
        
        
    


