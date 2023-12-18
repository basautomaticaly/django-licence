import hashlib
from datetime import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import License
from .serializers import LicenseSerializer




@api_view(['POST'])
def check_license(request):
    hwid = request.data.get('hwid')
    salt = 'ytsoft139392924992491dds'

    if hwid:
        try:
            license_obj = License.objects.get(user_hwid=hwid)
            serializer = LicenseSerializer(license_obj)
            today_date = datetime.now().date()

            if license_obj.expiration_date < today_date:
                return Response({'status': False})

            data_for_hash = f"{serializer.data['user_hwid']}"
            hwid_new = hashlib.md5((data_for_hash + salt).encode()).hexdigest()
            return Response({'status': True,
                             'hwid': hwid_new},
                            status=status.HTTP_200_OK)

        except License.DoesNotExist:
            return Response({'status': False})
    else:
        return Response({'error': 'Отсутствует параметр HWID'}, status=status.HTTP_400_BAD_REQUEST)
