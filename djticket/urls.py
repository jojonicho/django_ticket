"""djticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from api import views


from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
# router.register(r'movies', views.MovieViewSet, base_name='movies')
# router.register(r'seats', views.SeatViewSet, base_name='seats')
# router.register(r'orders', views.OrderViewSet, base_name='orders')
router.register(r'item', views.ItemViewSet)

schema_view = get_schema_view(title='Shopping API',
                              description='An API for fasilkom shopping :)')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    path('schema/', schema_view),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Tickets API'))
]
