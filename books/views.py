from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'detail.html', {'book': book})

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(publisher__icontains=query) |
            Q(ISBN__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'list.html', {'books': books})