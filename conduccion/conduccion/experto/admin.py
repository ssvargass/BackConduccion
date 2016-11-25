from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Field, FieldCondition, FieldType, FieldOption, Result
# Register your models here.

class FieldAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Field, FieldAdmin)
admin.site.register(FieldOption)
admin.site.register(FieldType)
admin.site.register(FieldCondition)
admin.site.register(Result)
