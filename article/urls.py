from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    # 文章详情
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article_create/', views.article_create, name='article_create'),
]
