from django.contrib import admin,messages
from .models import PricingConfiguration

class PricingConfigurationAdmin(admin.ModelAdmin):
    list_display = ['dbp', 'dap', 'tmf', 'wc', 'enabled', 'timestamp']

    def save_model(self, request, obj, form, change):
        # Perform custom validation checks before saving the object
        if obj.dbp < 0 or obj.dap < 0 or obj.tmf < 0 or obj.wc < 0:
            # If any value is negative, raise an exception and prevent saving
            messages.warning(request, "Values cannot be negative. Changes not saved.")
            return

        # Call the parent class's save_model method to save the object
        super().save_model(request, obj, form, change)
# Register your models here.
admin.site.register(PricingConfiguration, PricingConfigurationAdmin)