from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    path('', views.index, name='login')
]
