from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    SchemaListView,
    SchemaCreateView,
    SchemaUpdateView,
    SchemaDeleteView,
    DatasetView,
)

app_name = 'schemas'

urlpatterns = [
    path('', SchemaListView.as_view(), name='schema_list'),
    path('create/', SchemaCreateView.as_view(), name='schema_create'),
    path('<int:pk>/update/', SchemaUpdateView.as_view(), name='schema_update'),
    path('<int:pk>/delete/', SchemaDeleteView.as_view(), name='schema_delete'),
    path('<int:schema_pk>/data-sets/', DatasetView.as_view(), name='data_set'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
