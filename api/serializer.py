from rest_framework import serializers
from Store.models import User
from Store.models import Product

class Signup(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class loin_f(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField() 


class ProductSerilizer(serializers.ModelSerializer):
  class Meta:
      model=Product 
      fields='__all__'
      