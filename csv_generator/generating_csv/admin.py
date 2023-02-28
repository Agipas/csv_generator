from django.contrib import admin
from .models import *


class ColumnAdmin(admin.StackedInline):
    model = Column
    list_display = ('id', 'name', 'type', 'data_scheme', 'order')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
    extra = 1


class DataSchemeAdmin(admin.ModelAdmin):
    inlines = [ColumnAdmin]
    list_display = ('id', 'title', 'date_created', 'date_updated', 'author')
    list_display_link = ('id', 'title')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(DataScheme, DataSchemeAdmin)
admin.site.register(Column)
