from django.contrib import admin
from .models import Category, Task, SubTask


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'task')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)

