from django.urls import path
from NewApp import views

urlpatterns=[
    path('',views.home_page,name="Home"),
    path('About/',views.about_page,name="About"),
    path('Contact/',views.contact_page,name="Contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('our_products/',views.our_products,name="our_products"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('single_products/<int:prod_id>/',views.single_products,name="single_products"),
    path('register_page/',views.register_page,name="register_page"),
    path('save_register/',views.save_register,name="save_register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('delete_cart/<int:p_id>/',views.delete_cart,name="delete_cart"),
    path('user_login_page/',views.user_login_page,name="user_login_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('payment_page/',views.payment_page,name="payment_page"),
    path('save_placeorder/',views.save_placeorder,name="save_placeorder")
]