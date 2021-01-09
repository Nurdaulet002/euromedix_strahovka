from django.contrib import admin

# Register your models here.
from .models import Region, City, Bank, Insurance, Insurer,\
    Profile, Personification, Hospital, Profession

admin.site.register(Region)
admin.site.register(City)
admin.site.register(Bank)
admin.site.register(Insurance)
admin.site.register(Insurer)
admin.site.register(Profile)
admin.site.register(Personification)
admin.site.register(Hospital)
admin.site.register(Profession)
