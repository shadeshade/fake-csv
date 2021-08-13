from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SchemaListView, SchemaCreateView

app_name = 'schemas'

urlpatterns = [
    path('', SchemaListView.as_view(), name='schema_list'),
    path('create/', SchemaCreateView.as_view(), name='schema_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
