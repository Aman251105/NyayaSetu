from django.contrib import admin
from .models import (
    User,
    Prison,
    UTRC,
    UndertrialProfile,
    SupportPersonProfile,
    Notification,
    AuditLog,
    SystemSetting,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'role',
        'is_active',
        'created_at',
    )
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('role', 'is_active')


admin.site.register(Prison)
admin.site.register(UTRC)
admin.site.register(UndertrialProfile)
admin.site.register(SupportPersonProfile)
admin.site.register(Notification)
admin.site.register(AuditLog)
admin.site.register(SystemSetting)
