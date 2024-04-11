from django.db import models
from profiles.models import Profile 

class ServiceRequest(models.Model):
    employee = models.ForeignKey(Profile , on_delete=models.CASCADE , null= True)
    Location =  models.CharField(max_length= 50 , null= True)
    Department_choice = (
        ("SAC" , "SAC"),
        ("Engineering" , "Engineering"),
        ("SAP_SD" , "SAP_SD"),
        ("SAP_PP" , "SAP_PP"),
        ("SAP_MM" , "SAP_MM"),
        ("SAP_FICO" ,  "SAP_FICO"),
        ("SAP_ABAP" , "SAP_ABAP"),
    )
    Department = models.CharField(max_length= 50 , choices = Department_choice)
    Position_choice = (
        ("Trainee" , "Trainee"),
        ("Associate" , "Associate"),
        ("Consultant" , "Consultant"),
        ("Senior Associate" , "Senior Associate"),
        ("Manager" , "Manager"),
    )
    Position = models.CharField(max_length= 50 , choices= Position_choice)
    Date = models.DateTimeField()
    types = (
        ("Hardware" , "Hardware"),
        ("Software" , "Software"),
        ("Network Connectivity" , "Network Connectivity"),
        ("Technical_Support" , "Technical_Support"),
        ("Comaplaints" , "Complaints")
    )
    Requesttype = models.CharField(max_length=50 , choices = types)
    Manufacturer = models.TextField()
    Issue_Title = models.TextField()
    Description = models.TextField()
    Asset = models.IntegerField()
    STATUS = (
        ("Register" , "Register"),
        ("Assigned" , "Assigned"),
        ("Request_fulfiled" , "Request_fulfiled"),
        ("Aborted" , "Aborted"),
        ("Closed" , "Closed"),       
    )
    Status = models.CharField(max_length=50 , choices = STATUS)
    created = models.DateTimeField(auto_now_add=True, null = True)
    modify = models.DateTimeField(auto_now=True , null = True)