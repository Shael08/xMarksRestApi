from django.contrib import admin
from .models import Store
from .models import StoreType
from .models import OpeningHours

# Register your models here.

admin.site.register(Store)
admin.site.register(StoreType)
admin.site.register(OpeningHours)