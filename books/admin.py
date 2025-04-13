from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'ISBN', 'collection_count', 'remaining_stock')
    list_filter = ('publisher', 'author')
    search_fields = ('title', 'author', 'ISBN')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'translator', 'original_title', 'publisher', 'publication_info')
        }),
        ('内容信息', {
            'fields': ('content_summary', 'author_bio')
        }),
        ('出版信息', {
            'fields': ('page_count', 'price', 'binding', 'series', 'ISBN')
        }),
        ('库存信息', {
            'fields': ('collection_count', 'remaining_stock')
        }),
    )