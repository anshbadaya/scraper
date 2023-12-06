from django.urls import path
from .views import ProcessedItemList

urlpatterns = [
    path('processed-items/<int:page_number>/', ProcessedItemList.as_view(), name='processed-item-list'),
    
]
