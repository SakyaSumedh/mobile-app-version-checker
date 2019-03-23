from django.conf import settings

from rest_framework import mixins, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import MobileVersion
from .permissions import IsSuperUser
from .serializers import MobileVersionSerializer, CheckVersionSerializer


class MobileVersionViewset(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = MobileVersion.objects.all()
    serializer_class = MobileVersionSerializer
    permission_classes = [IsSuperUser, ]


class CheckVersionAPI(APIView):
    '''
    API to check mobile app's version.
    '''
    permission_classes = [AllowAny, ]

    def get_object(self, device_type):
        return MobileVersion.objects.get(device_type=device_type)

    def post(self, request):
        validated_data = CheckVersionSerializer().validate(request.data)
        try:
            mobile_version = self.get_object(validated_data.get('device_type', ''))
        except MobileVersion.DoesNotExist:
            return Response({
                "code": getattr(settings, 'ERROR_CODE'),
                "message": 'Device type doesn\'t exist.'
            }, status=status.HTTP_404_NOT_FOUND)

        if self.check_version(mobile_version, validated_data):
            return Response({
                "code": getattr(settings, 'SUCCESS_CODE'),
                "message": "Your app is up to date."
            }, status=status.HTTP_200_OK)

        data = {
            'code': getattr(settings, '{}'.format(
                'APP_UPDATE_OPTIONAL' if mobile_version.optional_update else 'APP_UPDATE_MANDATORY')),
            'message': "A newer version of app is available in store. Please update your app{}".format(
                " for better experience." if mobile_version.optional_update else "."),
            'app_link': mobile_version.app_link
        }
        return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def check_version(self, instance, data):
        if data['app_version'] == instance.app_version:
            return True
        return False
