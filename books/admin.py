from django.contrib import admin
from .models import Book,Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'datetime_creat', 'is_active', 'recomend']

admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)