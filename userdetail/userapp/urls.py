from django.urls import path
from userapp import views

urlpatterns = [
    path("",views.base,name='base'),
    path("home",views.home,name='home'),
    path("adin",views.adin,name='adin'),
    path("register",views.register,name='register'),
    path("user_login",views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name="user_logout"),
    path('user_update',views.User_update,name='user_update'),
    path("interest",views.interest,name="interest")
]