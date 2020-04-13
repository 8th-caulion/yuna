"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp1.views
import myapp2.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp1.views.main, name="main"),
    path('mymbti/', myapp1.views.mymbti, name="mymbti"),
    path('myreport/', myapp1.views.myreport, name="myreport"),
    path('mychildhood/', myapp1.views.mychildhood, name="mychildhood"),
    path('myfriends/', myapp2.views.myfriends, name="myfriends"),
]
