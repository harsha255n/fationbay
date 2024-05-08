from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from Store.models import Category,Product,cart,Ordermodel
from Store.forms import Regi,Loginform,orderform
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.
def Signin_required(fn):
     def wrrapper(request,*args,**kwargs):
          if not request.user.is_authenticated:
               return redirect("login")
          else:
             return fn(request,*args,**kwargs)
     return wrrapper       
             

class home(ListView):
   template_name="Store/index.html"
   model=Category
   context_object_name="categories"
    
# class Register(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"Store/register.html")
    

class Category_detail(View):
   def get(self,request,*args,**kwargs):
        id=kwargs.get("y")
        data=Product.objects.filter(category_id=id)
        to=Category.objects.get(id=id)
        return render(request,"Store/category_detail.html",{"product":data,"name":to})



class product_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("y")
        form=Product.objects.get(id=id)
        return render(request,"Store/productde.html",{"pro":form})

class Registerv(CreateView):
    template_name="Store/Registration.html"
    form_class=Regi
    model=User
    context_object_name="form"
    success_url=reverse_lazy("login")


class loginV(View):
    def get(self,request,*args,**kwargs):
        form= Loginform()
        return render(request,"Store/login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form= Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            u_pa=form.cleaned_data.get("password")
            u_obj=authenticate(request,username=u_name,password=u_pa)
            if u_obj:
                login(request,u_obj)
                print("entered suuccfully")
                return redirect("home") 
            else:
                print("error") 
                return redirect("login")     

         
    
class logoutV(View):
        def get(self,request,*args,**kwargs):
            logout(request)
            return redirect("login")
        

class Addcartv(View)    :

       def get(self,request,*args,**kwargs)    :
           id=kwargs.get("y")
           data=Product.objects.get(id=id)
           cart.objects.create(item=data,user=request.user)
           print("added")
           return redirect("cart")
           
class deletecart(View):
      def get(self,request,*args,**kwargs):
          id=kwargs.get("y")
          cart.objects.get(id=id).delete()
          return redirect("cart")

@method_decorator(Signin_required,name="dispatch")     
class cartdetail(View):
    def get(self,request,*args,**kwargs):
       
        data=cart.objects.filter(user=request.user)
       
        return render(request,"Store/cart.html",{"data":data})
    

class order_view(View):
    def get(self,request,*args,**kwargs):
           id=kwargs.get("y")
           data=Product.objects.get(id=id)
           form=orderform()
           return render(request,"Store/order.html",{"form":form,"data":data})
    
   
    def post(self,request,*args,**kwargs):
         id=kwargs.get("y")
         iq=orderform(request.POST)
         data=Product.objects.get(id=id)
         if iq.is_valid():
            qs=iq.cleaned_data.get("address")
            Ordermodel.objects.create(address=qs,order_item=data,customer=request.user)
            return redirect("home")    
         else:
             print("error")

         return redirect("home")  

@method_decorator(Signin_required,name="dispatch")     
class vieworder(View):
           def get(self,request,*args,**kwargs):
                data=Ordermodel.objects.filter(customer=request.user)
                return render(request,"Store/view_order.html",{"data":data})
           

class search_view(View):
     def get(self,request,*args,**kwargs):
          query = request.GET.get("q")

          if query:
               result=Product.objects.filter(name= query)


          else:
               result= None
          return render(request,"Store/search_result.html",{"result":result})
