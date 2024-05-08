from django.urls import path
from Store import views


urlpatterns = [
    
    path('home/',views.home.as_view(),name="home"),
    path('category/<int:y>',views.Category_detail.as_view(),name="category"),
    path('product/<int:y>',views.product_detail.as_view(),name="pro"),
    path('registration/',views.Registerv.as_view(),name="register"),
    path('login/',views.loginV.as_view(),name="login"),
    path('logout/',views.logoutV.as_view(),name="logout"),
    path('addtocart/<int:y>',views.Addcartv.as_view(),name="addcart"),
    path('delete/<int:y>',views.deletecart.as_view(),name="deletecart"),
    path('cart/',views.cartdetail.as_view(),name="cart"),
    path('order/<int:y>',views.order_view.as_view(),name="order"),
    path('orderpage/',views.vieworder.as_view(),name="orderpage"),
    path('search/',views.search_view.as_view(),name="srch"),
]
