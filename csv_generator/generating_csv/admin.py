from django.contrib import admin
from .models import *


class ColumnAdmin(admin.StackedInline):
    model = Column
    list_display = ('id', 'name', 'type', 'data_scheme', 'order')
    # list_display_links = ('id', 'name')
    extra = 1


class ColumnBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'data_scheme', 'order', 'range_from', 'range_to')
    list_display_links = ('id', 'name')
    search_field = ('id', 'type', 'data_scheme')
    list_editable = ('type', 'order', 'range_from', 'range_to')
    list_filter = ('type', 'data_scheme')


class DataSchemeAdmin(admin.ModelAdmin):
    inlines = [ColumnAdmin]
    list_display = ('id', 'title', 'date_created', 'date_updated', 'author', 'slug')
    list_display_links = ('id', 'title')
    search_field = ('id', 'title', 'slug')
    prepopulated_fields = {'slug': ('title', 'author')}
    list_editable = ('slug',)
    list_filter = ('author', 'date_created', 'date_updated')


class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_scheme', 'date_created', 'date_updated', 'file')
    list_display_links = ('id', 'data_scheme')
    search_field = ('id', 'file')
    list_filter = ('data_scheme', 'date_created', 'date_updated')


admin.site.register(DataScheme, DataSchemeAdmin)
# admin.site.register(Column)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Column, ColumnBaseAdmin)
