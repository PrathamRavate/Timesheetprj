# serializers.py
from rest_framework import serializers
from .models import ServiceRequest
from django.utils import timezone

class ServiceRequestSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    employee_name = serializers.SerializerMethodField()
    Location = serializers.CharField()
    Date = serializers.DateTimeField()  
    requested = serializers.SerializerMethodField()
    issue_title = serializers.CharField()  
    requesttype = serializers.CharField()  
    status = serializers.CharField()
    created = serializers.DateTimeField()

    def get_requested(self, obj):
        if obj.Date:
            request_time = timezone.now()
            time_diff = request_time - obj.Date
            days = time_diff.days
            if days == 0:
                return "Today"
            elif days == 1:
                return "Yesterday"
            else:
                return f"{days} Days Ago"
        else:
            return None
    
    def get_employee_name(self, obj):
        if obj.employee:
            return obj.employee.name
        return None
