from django.contrib import admin
from q_school.registration.models import Pax, SocialMediaAccount, SocialMediaPlatform

class PaxAdmin(admin.ModelAdmin):
    pass

class SocialMediaAccountAdmin(admin.ModelAdmin):
    pass

class SocialMediaPlatformAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pax, PaxAdmin)
admin.site.register(SocialMediaPlatform, SocialMediaPlatformAdmin)
admin.site.register(SocialMediaAccount, SocialMediaAccountAdmin)
