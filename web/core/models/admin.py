from django.contrib import admin
from models.models import *

# Register your models here.

admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(DocumentComment)
admin.site.register(Organization)
admin.site.register(Subdivision)
admin.site.register(SubSubDivision)
admin.site.register(Position)
admin.site.register(Event)
admin.site.register(CalendarSkip)
admin.site.register(CalendarVacation)
admin.site.register(EventType)
admin.site.register(Education)
admin.site.register(EducationType)
admin.site.register(News)