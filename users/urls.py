from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView  # 保留 LogoutView

urlpatterns = [
    path('login/', views.custom_login, name='login'),  # 使用自定义视图
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

