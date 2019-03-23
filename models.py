from django.db import models

DEVICE_TYPE = (
    ('1', 'IOS'),
    ('2', 'ANDROID')
)


class MobileVersion(models.Model):
    device_type = models.CharField(max_length=1, choices=DEVICE_TYPE)
    app_version = models.CharField(max_length=10)
    app_link = models.TextField()
    optional_update = models.BooleanField(default=True)
