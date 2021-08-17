from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SchemaListView, SchemaCreateView, SchemaDetailView, SchemaUpdateView, SchemaDeleteView, \
    JobCreateView

app_name = 'schemas'

urlpatterns = [
    path('', SchemaListView.as_view(), name='schema_list'),
    path('create/', SchemaCreateView.as_view(), name='schema_create'),
    path('<int:pk>', SchemaDetailView.as_view(), name='schema'),
    path('update/<int:pk>/', SchemaUpdateView.as_view(), name='schema_update'),
    path('delete/<int:pk>/', SchemaDeleteView.as_view(), name='schema_delete'),
    path('data-sets/<int:pk>/', JobCreateView.as_view(), name='job_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
