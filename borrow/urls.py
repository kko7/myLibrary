from django.urls import path
from . import views

app_name = 'borrow'

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
]
