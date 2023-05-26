from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from .serializer import OpeningSerializer
from .models import Opening


@api_view(['POST'])
def add_opening(request):
    headline = request.data.get('headline')
    description = request.data.get('description')
    pay = request.data.get('pay')
    level = request.data.get('level')
    job_type = request.data.get('job_type')
    requirements = request.data.get('requirements')
    company = request.user.company

    try:
        opening = Opening.objects.create(
            headline=headline,
            description=description,
            pay=pay,
            level=level,
            job_type=job_type,
            requirements=requirements,
            company=company
        )
        opening.save()
        return Response({
            "status": True,
            'message': 'Opening Successfully Created'
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            "status": False,
            'message': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_openings(request):
    openings = Opening.objects.all()
    serializer = OpeningSerializer(openings, many=True)
    return Response({
        "status": True,
        "data": {
            "openings": serializer.data
        },
        'message': 'Openings Successfully Fetched'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_opening(request, pk):
    opening = get_object_or_404(Opening, pk=pk)
    serializer = OpeningSerializer(opening)
    return Response({
        "status": True,
        "data": {
            "opening": serializer.data
        },
        'message': 'Opening Successfully Fetched'
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_opening(request, pk):
    opening = get_object_or_404(Opening, pk=pk)
    serializer = OpeningSerializer(opening, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "data": {
                "opening": serializer.data
            },
            'message': 'Opening Successfully Updated'
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_opening(request, pk):
    opening = get_object_or_404(Opening, pk=pk)
    opening.delete()
    return Response({
        "status": True,
        'message': 'Opening Successfully Deleted'
    }, status=status.HTTP_200_OK)
