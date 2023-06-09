from celery import shared_task
import datetime
from django.utils import timezone

from .models import Column, DataScheme, DataSet
from .utils import generate_csv_file


@shared_task()
def delete_data_set_without_file():
    return DataSet.objects.filter(file='', date_created__lt=timezone.now() + datetime.timedelta(minutes=-5)).delete()


@shared_task
def generate_csv(id, rows, data_set_id):
    columns = Column.objects.filter(data_scheme=id).order_by('order')
    scheme = DataScheme.objects.filter(pk=id).first()
    data_set = DataSet.objects.filter(pk=data_set_id).first()
    types = []
    range_from = []
    range_to = []
    for i in columns:
        types.append(i.type)
        range_from.append(i.range_from)
        range_to.append(i.range_to)
    is_file = generate_csv_file(types, range_from, range_to,
                                scheme.column_separator, scheme.string_character, scheme.title, rows)
    if is_file:
        data_set.file = is_file
        data_set.save()
        delete_data_set_without_file.apply_async((), countdown=60*5)
        return is_file
