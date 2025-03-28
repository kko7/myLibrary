from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='list/', permanent=True)),
    path('list/', views.book_list, name='book_list'),
    path('detail/<int:id>/', views.book_detail, name='book_detail'),
]
