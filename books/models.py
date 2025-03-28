from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="书名", db_index=True)
    author = models.CharField(max_length=100, verbose_name="作者", db_index=True)
    translator = models.CharField(max_length=100, verbose_name="译者", blank=True, null=True)
    original_title = models.CharField(max_length=255, verbose_name="原作名", blank=True, null=True)
    publisher = models.CharField(max_length=100, verbose_name="出版社")
    publication_info = models.TextField(verbose_name="出版信息", blank=True, null=True)
    content_summary = models.TextField(verbose_name="内容简介", blank=True, null=True)
    author_bio = models.TextField(verbose_name="作者简介", blank=True, null=True)
    page_count = models.PositiveIntegerField(verbose_name="页数", blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="定价", blank=True, null=True)
    binding = models.CharField(max_length=20, verbose_name="装帧", blank=True, null=True)
    series = models.CharField(max_length=100, verbose_name="所属丛书", blank=True, null=True)
    ISBN = models.CharField(max_length=17, verbose_name="ISBN", unique=True, db_index=True)
    collection_count = models.IntegerField(verbose_name="馆藏数量", default=0)
    remaining_stock = models.IntegerField(verbose_name="剩余库存", default=0)

    class Meta:
        db_table = "books_list"
        indexes = [
            models.Index(fields=["title"], name="idx_title"),
            models.Index(fields=["author"], name="idx_author"),
            models.Index(fields=["ISBN"], name="idx_ISBN"),
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(remaining_stock__lte=models.F("collection_count")), name="check_remaining_stock"),
        ]

    def __str__(self):
        return self.title
