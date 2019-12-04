from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,handler404, handler500
handler404 = 'votacoes.views.error404'
handler500 = 'votacoes.views.error500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('', include('votacoes.urls')),
]
