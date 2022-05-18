from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('reg_otp/',views.reg_otp,name="reg_otp"),
    path('forgot_pass/',views.forgot_pass,name="forgot_pass"),
    path('payment_module/',views.payment_module,name="payment_module"),

    





]