from django.contrib import admin
from borrow.models import BorrowRecord

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'due_date', 'is_returned')
    list_filter = ('is_returned',)
    search_fields = ('user__username', 'book__title')
