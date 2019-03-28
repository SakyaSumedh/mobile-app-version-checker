from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TestAppVersion(APITestCase):
    def setUp(self):
        self.url = reverse('check-version')

    def test_app_version_outdated_ios(self):
        response = self.client.post(self.url,
                                    data={'device_type': '1',
                                          'app_version': '0.1'})
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertIn('app_link', response.data)

    def test_app_version_updated_ios(self):
        response = self.client.post(self.url,
                                    data={'device_type': '1',
                                          'app_version': '1.0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_app_version_outdated_android(self):
        response = self.client.post(self.url,
                                    data={'device_type': '2',
                                          'app_version': '0.1'})
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertIn('app_link', response.data)

    def test_app_version_updated_android(self):
        response = self.client.post(self.url,
                                    data={'device_type': '2',
                                          'app_version': '1.0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_device_type(self):
        response = self.client.post(self.url,
                                    data={'device_type': '3',
                                          'app_version': '1.0'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
