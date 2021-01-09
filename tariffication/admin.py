from django.contrib import admin
from .models import Tariffication, Regiment, ProfessionHarm, ServiceHarm,\
    ServiceRegiment, Service

admin.site.register(Tariffication)
admin.site.register(Regiment)
admin.site.register(ProfessionHarm)
admin.site.register(ServiceHarm)
admin.site.register(ServiceRegiment)
admin.site.register(Service)
