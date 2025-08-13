from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.articulos.urls')),
    path('intercambios/', include('apps.intercambios.urls')),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change.html',
        success_url='/'
    ), name='password_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
