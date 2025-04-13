from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # 用户类型枚举
    ADMIN_LEVEL_CHOICES = [
        ('super', '超级管理员'),
        ('normal', '普通管理员'),
        ('none', '无权限'),
    ]

    # ---------- 基础字段 ----------
    name = models.CharField(
        _('姓名'),
        max_length=100,
        blank=True,
        help_text=_('用户的姓名')
    )

    id_card = models.CharField(
        _('身份证号'),
        max_length=18,
        blank=True,
        help_text=_('用户的身份证号码')
    )

    email = models.EmailField(
        _('电子邮箱'),
        max_length=254,
        unique=True,
        error_messages={
            'unique': _("该邮箱已被注册。"),
        }
    )

    phone = models.CharField(
        _('联系电话'),
        max_length=20,
        blank=True,
        help_text=_('请填写有效的手机号码')
    )

    # ---------- 权限字段 ----------
    admin_level = models.CharField(
        _('管理员级别'),
        max_length=10,
        choices=ADMIN_LEVEL_CHOICES,
        default='none',
        help_text=_('用户的管理权限级别')
    )

    is_librarian = models.BooleanField(
        _('馆员身份'),
        default=False,
        help_text=_('标记用户是否为图书馆工作人员')
    )

    # ---------- 权限系统适配 ----------
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('所属用户组'),
        blank=True,
        related_name="customuser_groups",
        related_query_name="customuser",
        help_text=_('用户所属的用户组')
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('用户权限'),
        blank=True,
        related_name="customuser_permissions",
        related_query_name="customuser",
        help_text=_('用户的特定权限')
    )

    class Meta:
        verbose_name = _('系统用户')
        verbose_name_plural = verbose_name
        ordering = ['-date_joined']
        permissions = [
            ("manage_normal_admin", "可以管理普通管理员"),
        ]

    def __str__(self):
        return f"{self.username} ({self.get_admin_level_display()})"

    # ---------- 属性方法 ----------
    @property
    def is_super_admin(self):
        return self.admin_level == 'super'

    @property
    def is_normal_admin(self):
        return self.admin_level == 'normal'

    # ---------- 业务逻辑 ----------
    def promote_to_admin(self, level='normal'):
        """提升用户为管理员"""
        if level == 'super':
            self.is_superuser = True
            self.is_staff = True
            self.admin_level = 'super'
        else:
            self.is_staff = True
            self.admin_level = 'normal'
        self.save()

    def demote_admin(self):
        """取消管理员权限"""
        self.is_staff = False
        self.is_superuser = False
        self.admin_level = 'none'
        self.save()