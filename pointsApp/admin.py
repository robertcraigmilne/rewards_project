from django.contrib import admin

# Register your models here.
from pointsApp.models import Members, Resorts, Points
admin.site.register(Members)
admin.site.register(Resorts)
admin.site.register(Points)
