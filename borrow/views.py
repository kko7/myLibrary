from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from books.models import Book
from borrow.models import BorrowRecord

@login_required
def record_list(request):
    records = BorrowRecord.objects.filter(user=request.user).select_related('book')
    return render(request, 'record_list.html', {'records': records})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.remaining_stock > 0:
        due = timezone.now().date() + timedelta(days=30)
        BorrowRecord.objects.create(user=request.user, book=book, due_date=due)
        book.remaining_stock -= 1
        book.save()
    return redirect('borrow:record_list')

@login_required
def return_book(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk, user=request.user)
    if not record.is_returned:
        record.return_date = timezone.now().date()
        record.is_returned = True
        record.save()
        book = record.book
        book.remaining_stock += 1
        book.save()
    return redirect('borrow:record_list')
