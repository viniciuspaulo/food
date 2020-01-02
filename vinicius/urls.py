
from django.contrib import admin
from django.urls import path, include


admin.site.index_template = 'food/dashboard/index.html'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("food.urls")),
]
