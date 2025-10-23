from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DataRecord
from .serializers import DataRecordSerializer

@api_view(['GET', 'PUT', 'PATCH'])
def data_record_view(request):
    obj, created = DataRecord.objects.get_or_create(
        id=1,
        defaults={
            'position': 1,
            'percent': 0.0,
            'year': 2025,
            'days': 0
        }
    )

    if request.method == 'GET':
        serializer = DataRecordSerializer(obj)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = DataRecordSerializer(obj, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
