from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Processed
from .serializers import ProcessedItemSerializer

class ProcessedItemList(APIView):
    def get(self, request,page_number):
        per_page = 20

        start_idx = (page_number - 1) * per_page
        end_idx = start_idx + per_page

        processed_items = Processed.objects.all().order_by('-time')[start_idx:end_idx]
        serializer = ProcessedItemSerializer(processed_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
