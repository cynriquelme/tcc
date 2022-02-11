"""appengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core.views import DashboardView, search
from crud import views as crud_views
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static
from registers.urls import registers_patterns
from reports.urls import reports_patterns

from django.conf import settings

urlpatterns = [
    path('', DashboardView.as_view(), name="home"),
    path('search/', core_views.search, name="search"),
    path('registers/', include(registers_patterns)),
    path('reports/', include(reports_patterns)),
    path('cities/', crud_views.list_cities, name='cities'),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

#Custom titles for admin
admin.site.site_header = "Atopa"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "Atopa"

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
