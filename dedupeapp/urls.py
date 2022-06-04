from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('dedupe_results', views.dedupe_results, name='dedupe_results'),
    path('get/results', views.DataTable.as_view(), name='get_results'),
    path('delete/record/', views.DeletView.as_view(), name='delete_record'),
    path('delete/record/<str:id>', views.DeletView.as_view(), name='delete_record'),
    path('', views.home, name='dedupeapp-home'), #Keep at bottom

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


#   href="{% url 'get_results' %}"