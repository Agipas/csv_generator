from time import sleep

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.core.cache import cache

from django.contrib import messages

from .decorators import user_not_authenticated
from .forms import LoginUserForm, DataSchemeColumnFormset, DataSchemeCreateForm
from .models import *
from .tasks import generate_csv


@login_required
def index(request):
    return render(request, 'base.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@method_decorator(user_not_authenticated, name='dispatch')
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def error_404_view(request, exception):
    return render(request, '404.html')


def new_scheme(request):
    if request.method == 'GET':
        schemes = DataScheme.objects.all()
        return render(request, 'data_scheme/create.html', {'schemes': schemes})


class DataSchemeList(ListView):
    model = DataScheme
    template_name = 'data_scheme.html'
    context_object_name = 'schemes'


class DataSchemeInline:
    form_class = DataSchemeCreateForm
    model = DataScheme
    template_name = "data_scheme/data_scheme_create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            form.add_error(None, "There were errors in the form.")
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()
        if not self.object.slug:
            self.object.slug = slugify(self.object.title) + self.object.author.username
            self.object.save()
        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        cache.delete('*schemes*')
        return redirect('list')

    def formset_columns_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        columns = formset.save(commit=False)  # self.save_formset(formset, contact)
        for obj in formset.deleted_objects:
            obj.delete()
        for column in columns:
            column.data_scheme = self.object
            column.save()


class DataSchemeCreate(DataSchemeInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(DataSchemeCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'columns': DataSchemeColumnFormset(prefix='columns'),
            }
        else:
            return {
                'columns': DataSchemeColumnFormset(self.request.POST or None, self.request.FILES or None, prefix='columns'),
            }


class DataSchemeUpdate(DataSchemeInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(DataSchemeUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'columns': DataSchemeColumnFormset(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='columns'),
        }


def delete_column(request, pk):
    try:
        column = Column.objects.get(id=pk)
    except Column.DoesNotExist:
        messages.success(request, 'Object Does not exit')
        # todo:change redirect
        return redirect('update_scheme', pk=column.product.id)

    column.delete()
    messages.success(request, 'Variant deleted successfully')
    # todo:change redirect
    return redirect('update_scheme', pk=column.product.id)


class DataSchemeDetail(DetailView):
    model = DataScheme
    template_name = 'data_scheme/data_scheme_info.html'
    context_object_name = 'data_scheme'
    slug_url_kwarg = 'scheme_slug'

    def get_context_data(self, **kwargs):
        context = super(DataSchemeDetail, self).get_context_data(**kwargs)
        context['columns'] = Column.objects.filter(data_scheme=self.get_object())
        context['datasets'] = DataSet.objects.filter(data_scheme=self.get_object())
        return context


def generate_dataset(request):
    if request.POST:
        scheme_id = int(request.POST['id'])
        rows = int(request.POST['rows'])
        scheme = DataScheme.objects.filter(pk=scheme_id).first()
        file = DataSet(data_scheme=scheme)
        file.save()
        numbers = DataSet.objects.filter(data_scheme=scheme_id).count()
        data = {
            'scheme': scheme.pk,
            'file': file.pk,
            'id': numbers,
            'date_created': file.date_created.strftime("%Y-%m-%d %H:%M")
        }
        generate_csv.delay(scheme.pk, rows, file.pk)
        return JsonResponse(data)


def get_file(request):
    if request.GET:
        scheme_id = int(request.GET['id'])
        while True:
            data_set = DataSet.objects.filter(pk=scheme_id).first()
            if data_set and data_set.file:
                data = {
                    'file': str(data_set.file),
                }
                return JsonResponse(data, safe=False)
            sleep(0.2)
