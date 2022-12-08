from django.urls import path
from . import views
app_name='common'

urlpatterns=[
    path('',views.homemenu, name="home"),
    
    path('menu/',views.getmenu, name="menu")
]