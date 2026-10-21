from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('all-topics/', all_topics, name='all_topics'),
    path('topico/<int:topico_id>/', topic_list, name='exibir_topico'),
    path('trilhas/', trilhas_list, name='trilhas_list'),
    path('trilhas/<slug:slug>/', trilha_detail, name='trilha_detail'),
    path('trilhas/etapa/<int:etapa_id>/toggle/', toggle_etapa, name='toggle_etapa'),
    path('conta/', conta, name='conta'),
    path('registro/', registro, name='registro'),
    path('login/', Class01LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('__reload__/', include('django_browser_reload.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
