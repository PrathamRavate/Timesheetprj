# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.utils import timezone

@api_view(['GET'])
def getServiceRequestsGroupedByDepartments(request):
    try:
        service_requests = ServiceRequest.objects.all()
        serialized_data = []
        for request in service_requests:
            serialized_data.append({
                'employee_id': request.employee_id,
                'employee_name': get_employee_name(request),
                'date': request.Date.strftime('%d/%m/%Y'),
                'requested': get_requested(request),
                'issue_title': request.Issue_Title,
                'Location' : request.Location,
                'requesttype': request.Requesttype,
                'status': request.Status
            })
        return Response({'applications_grouped_by_departments': serialized_data})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_requested(request):
    if request.Date:
            request_time = timezone.now()
            time_diff = request_time - request.Date
            days = time_diff.days
            if days == 0:
                return "Today"
            elif days == 1:
                return "Yesterday"
            else:
                return f"{days} Days Ago"
    else:
            return None
def get_employee_name(request):
    if request.employee:
        return request.employee.name
    return None