from django.contrib import admin
from django.urls import path, include
from .views import ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', ProductList.as_view()),
]
