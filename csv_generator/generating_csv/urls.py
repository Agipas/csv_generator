from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("login/", LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('list/', DataSchemePage.as_view(), name='list'),
    path('new_scheme/', new_scheme, name='new_scheme'),
    path('info/<slug:scheme>', index, name='scheme'),
    # path('<scheme>/update', scheme_update, name='scheme_update'),
    path('<scheme>/delete', index, name='scheme_delete'),
    # path('list/', home, name='list'),
]

handler404 = 'generating_csv.views.error_404_view'
