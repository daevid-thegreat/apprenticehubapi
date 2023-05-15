from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Application
from django.core.mail import send_mail
from .serializer import ApplicationSerializer



@api_view(['POST'])
def apply_for_opening(request):
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "data": {
                "application": serializer.data
            },
            'message': 'Application Successfully Created'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_applications(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response({
        "status": True,
        "data": {
            "applications": serializer.data
        },
        'message': 'Applications Successfully Fetched'
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    serializer = ApplicationSerializer(application)
    return Response({
        "status": True,
        "data": {
            "application": serializer.data
        },
        'message': 'Application Successfully Fetched'
    }, status=status.HTTP_200_OK)



@api_view(['PUT'])
def update_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    serializer = ApplicationSerializer(application, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "data": {
                "application": serializer.data
            },
            'message': 'Application Successfully Updated'
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.delete()
    return Response({
        "status": True,
        "data": {
            "application": None
        },
        'message': 'Application Successfully Deleted'
    }, status=status.HTTP_200_OK)