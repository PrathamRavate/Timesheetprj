from django.urls import path
from Servicereqs.views import getServiceRequestsGroupedByDepartments

urlpatterns = [
     path('getServiceRequestsGroupedByDepartments/', getServiceRequestsGroupedByDepartments, name='get_service_requests_grouped_by_departments'),
]