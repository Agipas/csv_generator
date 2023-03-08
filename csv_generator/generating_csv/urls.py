from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("login/", LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('list/', DataSchemeList.as_view(), name='list'),
    # path('info/<int:pk>', DataSchemeDetail.as_view(), name='scheme_info'),
    path('info/<slug:scheme_slug>', DataSchemeDetail.as_view(), name='scheme_info'),
    path('<scheme>/delete', index, name='scheme_delete'),
    path('create/', DataSchemeCreate.as_view(), name='create_scheme'),
    path('update/<int:pk>/', DataSchemeUpdate.as_view(), name='update_scheme'),
    path('delete-column/<int:pk>/', delete_column, name='delete_column'),
    path('generate-data/', generate_dataset, name='generate-data'),
    path('get-file/', get_file, name='get-file'),
]

handler404 = 'generating_csv.views.error_404_view'
