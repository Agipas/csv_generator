from django.contrib import admin
from .models import *


class ColumnAdmin(admin.TabularInline):
    model = Column
    list_display = ('id', 'name', 'type', 'data_scheme', 'order')
    extra = 1


class ColumnBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'data_scheme', 'order', 'range_from', 'range_to')
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'data_scheme')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (('order', 'range_from', 'range_to'),),
        }),
    )
    list_display_links = ('id', 'name')
    search_field = ('id', 'type', 'data_scheme')
    list_editable = ('type', 'order', 'range_from', 'range_to')
    list_filter = ('type', 'data_scheme')


class DataSchemeAdmin(admin.ModelAdmin):
    inlines = [ColumnAdmin]
    list_display = ('id', 'title', 'date_created', 'date_updated', 'author', 'slug', 'columns_count', 'is_data_set')
    list_display_links = ('id', 'title')
    search_field = ('id', 'title', 'slug')
    prepopulated_fields = {'slug': ('title', 'author')}
    list_editable = ('slug',)
    list_filter = ('author', 'date_created', 'date_updated')
    fieldsets = (
        (None, {
            'fields': ('title', 'author')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'date_created'),
        }),
    )

    @admin.display(description='Columns')
    def columns_count(self, obj):
        columns = Column.objects.filter(data_scheme=obj).count()
        return columns

    @admin.display(description='DataSet')
    def is_data_set(self, obj):
        data_set = DataSet.objects.filter(data_scheme=obj)
        return True if data_set else False
    is_data_set.boolean = True


class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_scheme', 'date_created', 'date_updated', 'file')
    list_display_links = ('id', 'data_scheme')
    search_field = ('id', 'file')
    list_filter = ('data_scheme', 'date_created', 'date_updated')


class CSVAdminSite(admin.AdminSite):
    site_header = "CSV admin"
    site_title = "CSV Admin Portal"
    index_title = "Welcome to Admin page"


csv_admin_site = CSVAdminSite(name='csv_admin')

csv_admin_site.register(DataScheme, DataSchemeAdmin)
csv_admin_site.register(DataSet, DataSetAdmin)
csv_admin_site.register(Column, ColumnBaseAdmin)
