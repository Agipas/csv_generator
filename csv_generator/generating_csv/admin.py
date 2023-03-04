from django.contrib import admin
from .models import *


class ColumnAdmin(admin.StackedInline):
    model = Column
    list_display = ('id', 'name', 'type', 'data_scheme', 'order')
    extra = 1


class DataSchemeAdmin(admin.ModelAdmin):
    inlines = [ColumnAdmin]
    list_display = ('id', 'title', 'date_created', 'date_updated', 'author', 'slug')
    prepopulated_fields = {'slug': ('title', 'author')}


class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'date_updated', 'data_scheme', 'file')


admin.site.register(DataScheme, DataSchemeAdmin)
admin.site.register(Column)
admin.site.register(DataSet, DataSetAdmin)
