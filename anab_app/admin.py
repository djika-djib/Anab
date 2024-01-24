from django.contrib import admin
from anab_app.models import UserProfileInfo, Partenaire, Service, Actu, DemandeSimple
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Partenaire)
admin.site.register(Service)
admin.site.register(Actu)
admin.site.register(DemandeSimple)


