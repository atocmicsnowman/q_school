from django.contrib import admin
from q_school.geography.models import Region, AreaOfOperation


class RegionAdmin(admin.ModelAdmin):
    pass


class AreaOfOperationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Region, RegionAdmin)
admin.site.register(AreaOfOperation, AreaOfOperationAdmin)
