from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class PricingConfiguration(models.Model):
    dbp = models.FloatField(default=0)  # Distance Base Price
    dap = models.FloatField(default=0)  # Distance Additional Price
    tmf = models.FloatField(default=0)  # Time Multiplier Factor
    wc = models.FloatField(default=0)   # Waiting Charges
    enabled = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.utcnow)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        if self.enabled:
            # Disable all other configurations
            PricingConfiguration.objects.exclude(id=self.id).update(enabled=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Configuration {self.id}"
