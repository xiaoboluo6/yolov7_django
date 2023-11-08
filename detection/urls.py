from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'web_app'
urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)