from django.db import models
from django.conf import settings
from books.models import Book
from datetime import timedelta, date


class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    #book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=date.today)
    #borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.borrow_date:
            self.borrow_date = date.today()
        # 自动计算 due_date 为 borrow_date + 30 天
        self.due_date = self.borrow_date + timedelta(days=30)
        super().save(*args, **kwargs)

    def _current_date(self):
        # 返回当前日期
        return models.DateField(auto_now_add=True).default

    def __str__(self):
        return f"{self.user.username} 借阅《{self.book.title}》"

    '''
    def save(self, *args, **kwargs):
        # 如果 borrow_date 没有被手动设置，则使用当前日期
        if not self.borrow_date:
            self.borrow_date = self._current_date()
        # 自动计算 due_date 为 borrow_date + 30 天
        self.due_date = self.borrow_date + timedelta(days=30)
        super().save(*args, **kwargs)
    '''