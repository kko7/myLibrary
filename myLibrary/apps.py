# myLibrary/apps.py
from django.apps import AppConfig
from django.contrib import admin

class MyLibraryConfig(AppConfig):
    name = 'myLibrary'

    def ready(self):
        admin.site.site_header = '书易通网上图书馆管理后台'
        admin.site.site_title = '书易通网上图书馆管理后台'
        admin.site.index_title = '书易通网上图书馆管理后台'