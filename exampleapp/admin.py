from django.contrib import admin
from exampleapp.models import AccessRecord,Topic,Webpage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)

