from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Catalog)
admin.site.register(NameProduct)
admin.site.register(Company)
admin.site.register(CompanyPhotos)