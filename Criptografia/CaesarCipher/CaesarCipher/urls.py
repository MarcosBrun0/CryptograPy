from django.contrib import admin
from django.urls import include, path
from cifra.views import home_view  # Importe a view da página inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Adicione esta linha
    path('cifra/', include('cifra.urls')),
]
