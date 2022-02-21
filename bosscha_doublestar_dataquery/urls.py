"""bosscha_doublestar_dataquery URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls import static, include

# from data_archive.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data_archive.urls')),
]

# urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = settings.SITE_HEADER # Django administration -> in <h1>
admin.site.site_title = settings.SITE_TITLE # Django site admin -> in <title>
admin.site.index_title = settings.ADMIN_INDEX_TITLE # Site administration -> Home Admin Title