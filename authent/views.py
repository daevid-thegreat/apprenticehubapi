import random
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from authent.serializer import NormalUserSerializer, MasterUserSerializer, CompanySerializer, UpdateSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from .models import OTP, User, Userprofile, Company
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from apprenticehubapi.settings import EMAIL_HOST_USER


@api_view(['GET'])
def check_auth(request):
    return Response({
        'status': True,
        'data': {
            'user': NormalUserSerializer(request.user).data,
            'tel': request.user.tel,

        }
    })


@api_view(['POST'])
def generate_otp(request):
    email = request.data.get('email')
    user = get_object_or_404(User, email=email)
    otp = ''.join(random.choices('0123456789', k=6))
    OTP.objects.create(user=user, otp=otp)
    # send the OTP code to the user's email or phone number
    return Response({'message': 'OTP has been sent to your email/phone number'})


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def signup(request):
    serializer = NormalUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.create(serializer.validated_data)
        otp = ''.join(random.choices('0123456789', k=6))
        OTP.objects.create(user=user, otp=otp)

        send_mail(
            'Welcome to MyApprenticeHub',
            'Verify Your Email, Here is your OTP : {}'.format(otp),
            EMAIL_HOST_USER,
            [user.email],
        )

        response = Response({
            "status": True,
            "data": {
                "user": serializer.data
            },
            'message': 'User Account Successfully Created'
        }, status=status.HTTP_201_CREATED)

        return response

    elif Userprofile.objects.filter(email=request.data.get('email')).exists():
        response = Response({
            "status": False,
            "data": {},
            'message': 'User already exists... Kindly sign in'
        }, status=status.HTTP_400_BAD_REQUEST)
        return response
    else:
        response = Response({
            "status": False,
            "data": {},
            'message': 'Something is wrong... Kindly try again'
        }, status=status.HTTP_400_BAD_REQUEST)
        return response


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def signup_master(request):
    serializer = MasterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.create(serializer.validated_data)
        user.is_master = True
        user.save()
        otp = ''.join(random.choices('0123456789', k=6))
        OTP.objects.create(user=user, otp=otp)

        send_mail(
            'Welcome to MyApprenticeHub',
            'Verify Your Email, Here is your OTP : {}'.format(otp),
            EMAIL_HOST_USER,
            [user.email],
        )

        response = Response({
            "status": True,
            "data": {
                "user": serializer.data
            },
            'message': 'User Account Successfully Created'
        }, status=status.HTTP_201_CREATED)

        return response

    elif Userprofile.objects.filter(email=request.data.get('email')).exists():
        response = Response({
            "status": False,
            "data": {},
            'message': 'User already exists... Kindly sign in'
        }, status=status.HTTP_400_BAD_REQUEST)
        return response
    else:
        response = Response({
            "status": False,
            "data": {},
            'message': 'Something is wrong... Kindly try again'
        }, status=status.HTTP_400_BAD_REQUEST)
        return response


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        Userprofile.objects.get(email=email)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({
                "status": False,
                "data": {},
                'message': 'Invalid Credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
        if user.is_active:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            response = Response({
                "status": True,
                "data": {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "name": user.name,
                        "is_master": user.is_master,
                    },
                    "token": token.key
                },
                'message': 'User Account Successfully Logged In'
            }, status=status.HTTP_200_OK)
            response.set_cookie(key='jwt', value=token.key, httponly=True)
            return response

        else:
            return Response({
                "status": False,
                "data": {},
                'message': 'User Account is not active, reach out to admin'
            }, status=status.HTTP_400_BAD_REQUEST)

    except Userprofile.DoesNotExist:
        return Response({
            "status": False,
            "data": {},
            'message': 'User does not exist'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def update_user(request):
    user = request.user
    serializer = UpdateSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response = Response({
            "status": True,
            "data": {
                "user": serializer.data
            },
            'message': 'User Account Successfully Updated'
        }, status=status.HTTP_200_OK)
        return response
    else:
        response = Response({
            "status": False,
            "data": {},
            'message': 'Something is wrong... Kindly try again'
        }, status=status.HTTP_400_BAD_REQUEST)
        return response


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def verify_email(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    user = Userprofile.objects.get(email=email)
    otp_obj = OTP.objects.filter(
        user=user, otp=otp, is_used=False, is_expired=False).order_by('-created_at').first()
    if otp_obj:
        otp_obj.is_used = True
        otp_obj.save()
        user.is_verified = True
        user.save()
        return Response({'message': 'Verified successfully'})
    else:
        return Response({'message': 'Invalid OTP or OTP has already been used'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_password(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    user = get_object_or_404(User, email=email)
    otp_obj = OTP.objects.filter(
        user=user, otp=otp, is_used=False).order_by('-created_at').first()
    if otp_obj:
        otp_obj.is_used = True
        otp_obj.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({
            "status": True,
            "data": {
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_master": user.is_master,
                },
            },
        })
    else:
        return Response({'message': 'Invalid OTP or OTP has already been used'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def change_password(request):
    email = request.data.get('email')
    password = request.data.get('password')
    old_password = request.data.get('old_password')
    try:
        user = Userprofile.objects.get(email=email)
        if user.check_password(old_password):
            user.set_password(password)
            user.save()
            return Response({
                "status": True,
                "data": {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "name": user.name,
                        "is_master": user.is_master,
                    },
                },
                'message': 'Password Successfully Changed'

            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)
    except Userprofile.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_company(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = Response({
            "status": True,
            "data": {
                "company": serializer.data
            },
            'message': 'Company Successfully Added'
        }, status=status.HTTP_201_CREATED)
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def resend_email_otp(request):
    email = request.data.get('email')
    user = Userprofile.objects.get(email=email)
    otp = ''.join(random.choices('0123456789', k=6))
    OTP.objects.create(user=user, otp=otp)
    send_mail(
        'OTP for email verification',
        f'Your OTP is {otp}',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return Response({'message': 'OTP sent successfully'})


@api_view(['POST'])
@permission_classes([AllowAny])
def addCompany(request):
    user = request.user
    try:
        c = Company.objects.create(
            name=request.data.get('name'),
            logo=request.data.get('logo'),
            city=request.data.get('city'),
            state=request.data.get('state'),
            industry=request.data.get('industry'),
            description=request.data.get('description'),
            website=request.data.get('website'),
            facebook=request.data.get('facebook'),
            twitter=request.data.get('twitter'),
            linkedin=request.data.get('linkedin'),
            instagram=request.data.get('instagram'),

            user=user,
        )
        c.save()
        return Response({
            "status": True,
            "data": {
                "company": {
                    "id": c.id,
                    "name": c.name,
                },
            },
        })
    except Exception as e:
        return Response({
            "status": False,
            "message": str(e)
        })


@api_view(['POST'])
@permission_classes([AllowAny])
def updateCompany(request):
    user = request.user
    try:
        company = Company.objects.get(user=user)
        company.name = request.data.get('name')
        company.logo = request.data.get('logo')
        company.city = request.data.get('city')
        company.state = request.data.get('state')
        company.industry = request.data.get('industry')
        company.description = request.data.get('description')
        company.website = request.data.get('website')
        company.facebook = request.data.get('facebook')
        company.twitter = request.data.get('twitter')
        company.linkedin = request.data.get('linkedin')
        company.instagram = request.data.get('instagram')
        company.save()
        return Response({
            "status": True,
            "data": {
                "company": {
                    "id": company.id,
                    "name": company.name,
                },
            },
        })
    except Company.DoesNotExist:
        return Response({'message': "You don't have a company yet"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([AllowAny])
def getCompany(request):
    user = request.user
    try:
        company = Company.objects.get(user=user)
        return Response({
            "status": True,
            "data": {
                "company": {
                    "id": company.id,
                    "logo": company.logo,
                    "name": company.name,
                    "city": company.city,
                    "state": company.state,
                    "industry": company.industry,
                    "description": company.description,
                    "facebook": company.facebook,
                    "twitter": company.twitter,
                    "linkedin": company.linkedin,
                    "instagram": company.instagram
                },
            },
        })
    except Company.DoesNotExist:
        return Response({'message': "You don't have a company yet"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def deleteCompany(request):
    user = request.user
    try:
        company = Company.objects.get(user=user)
        company.delete()
        return Response({'message': 'Company deleted successfully'})
    except Company.DoesNotExist:
        return Response({'message': "You don't have a company yet"}, status=status.HTTP_204_NO_CONTENT)
