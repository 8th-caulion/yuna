from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('<int:blog_id>/', blog.views.detail, name='detail'),
    #detail url이 <int:blog_id>인 이유는 클릭하는 object의 data에 따라 url이 달라지기 때문
    path('new/', blog.views.new, name='new'),
    path('create/', blog.views.create, name='create'),
    path('edit/<int:blog_id>/', blog.views.edit, name="edit"),
    path('update/<int:blog_id>/', blog.views.update, name="update"),
    path('delete/<int:blog_id>/', blog.views.delete, name="delete"),
]