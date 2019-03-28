from django.core.management.base import BaseCommand

from mobile_version_app.models import MobileVersion


class Command(BaseCommand):
    help = "Load default data for Mobile applications' version details."

    @staticmethod
    def add_mobile_version_details():
        # IOS
        MobileVersion.objects.create(device_type='1', app_version='1.0',
                                     app_link='http://bl.ocks.org/d3indepth/b6d4845973089bc1012dec1674d3aff8')
        
        # ANDROID
        MobileVersion.objects.create(device_type='2', app_version='1.0',
                                     app_link='https://bl.ocks.org/d3noob/ced1b9b18bd8192d2c898884033b5529')

    def handle(self, *args, **options):
        self.add_mobile_version_details()