import json
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from apprenticehubapi.settings import EMAIL_HOST_USER
from authent.models import Company
from .serializer import OpeningSerializer, ApplicationSerializer
from .models import Opening, Application, Apprentice
from authent.models import Userprofile


@api_view(['POST'])
def add_opening(request):
    try:
        c = Company.objects.get(user=request.user)
        headline = request.data.get('headline')
        description = request.data.get('description')
        pay = request.data.get('pay')
        level = request.data.get('level')
        job_type = request.data.get('job_type')
        company = c

        try:
            opening = Opening.objects.create(
                headline=headline,
                description=description,
                pay=pay,
                level=level,
                job_type=job_type,
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
    except Company.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Company Does Not Exist'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_my_openings(request):
    try:
        c = Company.objects.get(user=request.user)
        openings = Opening.objects.filter(company=c)
        serializer = OpeningSerializer(openings, many=True)

        return Response({
            "status": True,
            "data": {
                "openings": serializer.data
            },
            'message': 'Openings Successfully Fetched'
        }, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Company Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
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
@permission_classes([AllowAny])
@authentication_classes([])
def get_opening(request, uid):
    try:
        opening = Opening.objects.get(uid=uid)
        serializer = OpeningSerializer(opening)
        return Response({
            "status": True,
            "data": {
                "opening": serializer.data,
                "company": {
                    "name": opening.company.name,
                    "industry": opening.company.industry,
                    "bio": opening.company.description,
                    "website": opening.company.website,
                    "facebook": opening.company.facebook,
                    "twitter": opening.company.twitter,
                    "linkedin": opening.company.linkedin,
                    "instagram": opening.company.instagram,
                }
            },
            'message': 'Opening Successfully Fetched'
        }, status=status.HTTP_200_OK)
    except Opening.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Opening Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_opening(request, uid):

    try:
        opening = get_object_or_404(Opening, uid=uid)
        headline = request.data.get('headline')
        description = request.data.get('description')
        pay = request.data.get('pay')
        level = request.data.get('level')
        job_type = request.data.get('job_type')

        if headline:
            opening.headline = headline
        if description:
            opening.description = description
        if pay:
            opening.pay = pay
        if level:
            opening.level = level
        if job_type:
            opening.job_type = job_type
        opening.save()

        return Response({
            "status": True,
            'message': 'Opening Successfully Updated'
        }, status=status.HTTP_200_OK)
    except Opening.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Opening Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)



    # serializer = OpeningSerializer(opening, data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response({
    #         "status": True,
    #         "data": {
    #             "opening": serializer.data
    #         },
    #         'message': 'Opening Successfully Updated'
    #     }, status=status.HTTP_200_OK)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_opening(request, uid):
    try:
        opening = get_object_or_404(Opening, uid=uid)
        opening.delete()
        return Response({
            "status": True,
            'message': 'Opening Successfully Deleted'
        }, status=status.HTTP_200_OK)
    except Opening.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Opening Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def apply_opening(request, uid):
    try:
        opening = Opening.objects.get(uid=uid)
        user = request.user
        email = request.data.get('email')
        education = request.data.get('education')
        age = request.data.get('age')
        tel = request.data.get('tel')
        info = request.data.get('message')
        application = Application.objects.create(
            opening=opening,
            user=user,
            email=email,
            education=education,
            age=age,
            tel=tel,
            message=info
        )
        application.save()
        send_mail(
            'New Application',
            'You have a new application',
            EMAIL_HOST_USER,
            [opening.company.user.email],
            fail_silently=False,
        )
        send_mail(
            'Application Received',
            'Your application has been received',
            EMAIL_HOST_USER,
            [user.email],
        )
        return Response({
            "status": True,
            'message': 'Application Successfully Created'
        }, status=status.HTTP_201_CREATED)
    except Opening.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Opening Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_applications(request):
    try:
        c = Company.objects.get(user=request.user)
        openings = Opening.objects.filter(company=c)
        apps = Application.objects.filter(opening__in=openings)

        return Response({
            "status": True,
            "data": {
                "applications": apps
            },
            'message': 'Applications Successfully Fetched'
        }, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Company Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_my_applications(request):
    applications = []
    try:
        user = request.user
        apps = Application.objects.filter(user=user)
        for app in apps:
            applications[app.opening.uid] = {
                "headline": app.opening.headline,
                "username": app.user.name,
                "date": app.date
            }

        return Response({
            "status": True,
            "data": {
                "applications": applications
            },
            'message': 'Applications Successfully Fetched'
        }, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Company Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_apprentice(request):
    try:
        company = Company.objects.get(user=request.user)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        pay = request.data.get('pay')
        apprentice = Apprentice.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            pay=pay,
            company=company
        )
        apprentice.save()
        send_mail(
            'New Apprentice',
            'You have a new apprentice',
            EMAIL_HOST_USER,
            [company.user.email],
        )
        send_mail(
            'Apprentice Received',
            'You have been received as an apprentice',
            EMAIL_HOST_USER,
            [email],
        )
        return Response({
            "status": True,
            'message': 'Apprentice Successfully Created'
        }, status=status.HTTP_201_CREATED)
    except Company.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Company Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_apprentice(request, uid):
    try:
        apprentice = get_object_or_404(Apprentice, uid=uid)
        apprentice.delete()
        return Response({
            "status": True,
            'message': 'Apprentice Successfully Deleted'
        }, status=status.HTTP_200_OK)
    except Apprentice.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Apprentice Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_apprentices(request):
    try:
        company = Company.objects.get(user=request.user)
        apprentices = Apprentice.objects.filter(company=company)
        return Response({
            "status": True,
            "data": {
                "apprentices": apprentices
            },
            'message': 'Apprentices Successfully Fetched'
        }, status=status.HTTP_200_OK)
    except Company.DoesNotExist:
        return Response({
            "status": False,
            'message': 'Company Does Not Exist'
        }, status=status.HTTP_204_NO_CONTENT)
