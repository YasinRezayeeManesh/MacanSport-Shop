from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'user', 'parent', 'success']
