"""
URL configuration for DakongSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# URL Configuration (urls.py)
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

# add appliaction
urlpatterns += [
    path('', include('WebSite.urls')),
    path('account/', include('Accounts.urls')),
    path('news/', include('News.urls')),
    path('products/', include('Products.urls')),
    path('media/', include('Media.urls')),
]

# # Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]

if(settings.DEBUG):
    # Use static() to add url mapping to serve static files during development (only)
    
    from django.conf.urls.static import static
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)