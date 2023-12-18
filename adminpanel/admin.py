from django.contrib import admin
from django.utils import timezone
from .models import License


class ExpiredLicenseFilter(admin.SimpleListFilter):
    title = 'Истекшие лицензии'
    parameter_name = 'expired'

    def lookups(self, request, model_admin):
        return (
            ('expired', 'Истекшие лицензии'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'expired':
            today = timezone.now().date()
            return queryset.filter(expiration_date__lt=today)


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('user_tg', 'user_hwid', 'expiration_date')
    list_filter = ('expiration_date', ExpiredLicenseFilter)
    search_fields = ('user_tg', 'user_hwid')


admin.site.register(License, LicenseAdmin)
