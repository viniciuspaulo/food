from django.contrib import admin
from .models import *

admin.site.site_header = "Admin Food"


admin.site.register(Category)
# admin.site.register(Company)
admin.site.register(Product)