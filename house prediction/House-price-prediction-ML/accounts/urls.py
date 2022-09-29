from . import views
from django.urls import URLPattern, include, path

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('sproduct',views.sproduct,name="sproduct"),
    path('liked',views.likedd,name='liked'),
    path('likedpages',views.likedpages,name='likedpages'),
    path('productsearch',views.productsearch,name='productsearch'),
    path('cpass',views.cpass,name='cpass'),
    path('logoutuser',views.logoutuser,name='logout'),
]