# Generated by Django 5.1.2 on 2025-04-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(db_index=True, max_length=255, verbose_name="书名"),
                ),
                (
                    "author",
                    models.CharField(db_index=True, max_length=100, verbose_name="作者"),
                ),
                (
                    "translator",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="译者"
                    ),
                ),
                (
                    "original_title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="原作名"
                    ),
                ),
                ("publisher", models.CharField(max_length=100, verbose_name="出版社")),
                (
                    "publication_info",
                    models.TextField(blank=True, null=True, verbose_name="出版信息"),
                ),
                (
                    "content_summary",
                    models.TextField(blank=True, null=True, verbose_name="内容简介"),
                ),
                (
                    "author_bio",
                    models.TextField(blank=True, null=True, verbose_name="作者简介"),
                ),
                (
                    "page_count",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="页数"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="定价",
                    ),
                ),
                (
                    "binding",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="装帧"
                    ),
                ),
                (
                    "series",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="所属丛书"
                    ),
                ),
                (
                    "ISBN",
                    models.CharField(
                        db_index=True, max_length=17, unique=True, verbose_name="ISBN"
                    ),
                ),
                (
                    "collection_count",
                    models.IntegerField(default=0, verbose_name="馆藏数量"),
                ),
                (
                    "remaining_stock",
                    models.IntegerField(default=0, verbose_name="剩余库存"),
                ),
            ],
            options={
                "db_table": "books_list",
                "indexes": [
                    models.Index(fields=["title"], name="idx_title"),
                    models.Index(fields=["author"], name="idx_author"),
                    models.Index(fields=["ISBN"], name="idx_ISBN"),
                ],
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(
                            ("remaining_stock__lte", models.F("collection_count"))
                        ),
                        name="check_remaining_stock",
                    )
                ],
            },
        ),
    ]
