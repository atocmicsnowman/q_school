from django.contrib import admin
from q_school.geography.models import (
    Region, AreaOfOperation, AreaOfOperationFlavor, AreaOfOperationType
)


class RegionAdmin(admin.ModelAdmin):
    pass


class AreaOfOperationAdmin(admin.ModelAdmin):
    pass


class AreaOfOperationTypeAdmin(admin.ModelAdmin):
    pass


class AreaOfOperationFlavorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Region, RegionAdmin)
admin.site.register(AreaOfOperation, AreaOfOperationAdmin)
admin.site.register(AreaOfOperationType, AreaOfOperationTypeAdmin)
admin.site.register(AreaOfOperationFlavor, AreaOfOperationFlavorAdmin)
